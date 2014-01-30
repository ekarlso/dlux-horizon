/*horizonApp.controller('OvsdbController', ['$scope', function($scope) {
    $scope.greeting = 'Hola!';
}]);*/

// Load UI Router
horizonApp.requires.push('ui.router');

horizonApp.controller('OVSDBNavCtrl', function($scope) {

})

horizonApp.config(function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise("/");
    $stateProvider.state('table', {
        url: '/table',
        template: 'Click on table to the left to view.'
    })

    $stateProvider.state('table.rows', {
        url: '/{name}',
        views: {
            '@': {
                templateUrl: '/static/partials/ovsdb/rows.html',
                controller: function($scope, $state, $http) {
                    $http.get('ovsdb/' + $scope.$stateParams.name).success(function(data) {
                        $scope.headers = data.table.headers
                        $scope.rows = data.table.rows
                    });
                }
            }
        }
    })
})

// NOTE(ekarlso): Is there a better way to do this?
horizonApp.run(
    ['$rootScope', '$state', '$stateParams',
    function($rootScope, $state, $stateParams) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;
}])