'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('PhoneListCtrl', function($scope, $http) {
  $http.get('phones/get_phone_json').success(function(data) {
    console.log(data);
    $scope.phones = data;
  });

  $scope.orderProp = 'age';
});
