// Generated by CoffeeScript 1.9.2
(function() {
  angular.module("Customer", ['ngResource', 'ngRoute']).constant('SIGNIN_URL', '/signin/').constant('SIGNUP_URL', '/signup/').config(function($routeProvider, SIGNIN_URL, SIGNUP_URL) {
    return $routeProvider.when(SIGNUP_URL, {
      templateUrl: window.ng_config.static_url + "js/app/site/view/signup.html"
    });
  });

}).call(this);
