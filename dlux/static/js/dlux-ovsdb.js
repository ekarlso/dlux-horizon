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

    $stateProvider.state('table.bridge', {
        url: '/bridge',
        views: {
            '@': {
                templateUrl: '/static/partials/ovsdb/bridge_rows.html',
                controller: function($scope, $http) {
                    $http.get('ovsdb/bridge').success(function(data) {
                        $scope.rows = data.rows
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