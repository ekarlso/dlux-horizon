// Service to register all garph directives on a page.
// TODO(ekarlso): Make functions only return the graph ?
angular.module('horizonApp').service('graphService', [function () {
    var svc = {i: 0};

    svc.graphs = {};

    /*
        Register a graph by name
    */
    svc.registerGraph = function(name, graphDirective) {
        svc.graphs[name] = graphDirective;
    };

    /*
        Update a Graph by name and data
    */
    svc.updateBySeries = function(graphname, data, ignoreUnknown) {
        var graphDirective = svc.graphs[graphname]
        // Don't bother trying to update if the graph isn't init'ed yet.
        if (!graphDirective) {
            return
        }

        if (ignoreUnknown === undefined && graphDirective.ignoreUnknown !== undefined) {
            ignoreUnknown = graphDirective.ignoreUnknown
        }

        angular.forEach(data, function(value, name) {
            if (ignoreUnknown && !graphDirective.graph.series.itemByName(name)) {
                return
            }

            obj = {}
            obj[name] = value
            graphDirective.graph.series.addData(obj)
        })
        graphDirective.graph.update()
    };

    /*
        Take an array like {myGraph: {serie1: [], serie2: []}} and update accordingly.
    */
    svc.updateByObject = function(object, ignoreUnknown) {
        angular.forEach(object, function(data, graphName) {
            svc.updateBySeries(graphName, data, ignoreUnknown)
        })
    }

    /*
        Get a Graph Directive
    */
    svc.getGraph = function (name) {
        return svc.graphs[name]
    }

    return svc
}]);


angular.module('horizonApp').directive('rickshawGraph', ['$timeout', 'graphService', function($timeout, graphService) {
    return {
        restrict: 'E',
        templateUrl: '/static/partials/directives/graph.html',
        scope: {
            'series': '=',
            'width': '=',
            'height': '=',
            'type': '=',
            'name': '=',
            'interval': '=',
            'ignoreUnknown': '='
        },

        link: function($scope, iElm, iAttrs, controller) {
            // Fire off the initial series data
            var element = iElm.find('#graph')[0]

            var height = $scope.height || "100";
            var width = $scope.width || "300";
            var type = $scope.type || 'line';
            var interval = $scope.interval || 1;

            $scope.$watch('series', function (value) {
                if (!value) {
                    return
                }

                var series = new Rickshaw.Series(
                    value,
                    undefined,
                    {
                        timeInterval: interval * 1000,
                        tiemBase: new Date().getTime() / 1000
                    }
                )

                $scope.graph = new Rickshaw.Graph({
                    element: element,
                    height: height,
                    width: width,
                    renderer: type,
                    series: series,
                });

                $scope.graph.render();

                var x_axis = new Rickshaw.Graph.Axis.Time({
                    graph: $scope.graph
                })

                x_axis.render()

                var y_axis = new Rickshaw.Graph.Axis.Y({
                    graph: $scope.graph,
                })

                y_axis.render()

                var legend = new Rickshaw.Graph.Legend({
                    graph: $scope.graph,
                    element: iElm.find('#graph_legend')[0]
                })

                var shelving = new Rickshaw.Graph.Behavior.Series.Toggle( {
                    graph: $scope.graph,
                    legend: legend
                });

                var hoverDetail = new Rickshaw.Graph.HoverDetail( {
                    graph: $scope.graph
                } );
            })

            $scope.$watch('height', function(value){
                if (value !== undefined && $scope.graph != null) {
                  $scope.graph.setSize({height: value, width: $scope.graph.width});
                  $scope.graph.update();
                }
            });

            $scope.$watch('width', function(value){
                if (value !== undefined && $scope.graph != null) {
                    $scope.graph.setSize({height: $scope.graph.height, width: value});
                    $scope.graph.update();
                }
            });

            $scope.$watch('type', function (value) {
                if (value !== undefined && $scope.graph !== undefined) {
                    $scope.graph.setRenderer(value)
                    $scope.graph.update()
                }
            })

            // Watch and handle interval, clearing any series data if it changes
            $scope.$watch('interval', function (value) {
                if ($scope.interval === $scope.graph.timeInterval) {
                    return
                }

                $scope.graph.series.setTimeInterval(value * 1000)

                angular.forEach($scope.graph.series, function (serie) {
                    serie.data = []
                })

                $scope.graph.update()
            })

            $scope.$watch(function() {return $scope.graph.series.getIndex()}, function (value) {
                $scope.index = value;
            })

            // Register ourselves to the graphService
            if ($scope.name) {
                graphService.registerGraph($scope.name, $scope)
            }
        }
    };
}]);


angular.module('horizonApp').controller('ControllerStatsCtrl', ['$scope', '$http', '$timeout', '$q', 'graphService', function ($scope, $http, $timeout, $q, graphService) {
    $scope.interval = 1;
    $scope.sequence = 0

    $scope.getStats = function () {
        $http.get('stats').success(function(data) {
            $scope.stats = data;

            graphService.updateBySeries('threading', data.threading)

            graphService.updateByObject($scope.stats.memory)
            //graphService.updateByObject($scope.stats.threading)

            //debugger
            //graphService.updateGraph('memory', {used: $scope.stats.memory.NonHeapMemoryUsage.used})
        })
    }
    $scope.getStats()

    $scope.update = function () {
        $scope.current = $timeout(function() {
            $scope.getStats()
            $scope.update();
        }, $scope.interval*1000)
    }
    $scope.update()

    $scope.changeInterval = function (interval) {
        // Only bother changing if it's not like the current.
        if (interval !== $scope.interval) {
            // Cancel any current promise so it doesn't exec
            if ($scope.current) {
                $timeout.cancel($scope.current)
            }

            $scope.interval = interval;

            // Start the updating again
            $scope.update();
        }
    }

    $scope.title = "Test Angular Rickshaw";
    $scope.graphheight = 100;
    $scope.graphwidth = 100;

    $scope.memoryNonHeap = [
        {
            name: 'used',
            color: 'gold',
            data: []
       }

    ]
    $scope.memoryHeap = [
        {
            name: 'used',
            color: 'gold',
            data: []
        }
    ]

    $scope.threadingGraph = [
        {
            name: 'ThreadCount'
        },
        /*{
            name: 'DaemonThreadCount'
        },
        {
            name: 'PeakThreadCount'
        },
        {
            name: 'Current',
        }*/
    ]
}])
