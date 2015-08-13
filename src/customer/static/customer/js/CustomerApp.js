// Generated by CoffeeScript 1.9.2
(function() {
  angular.module("Customer", ['ngResource', 'ngRoute']).constant('CUSTOMER_API_URL', window.ng_config.api + "/customer").constant('CUSTOMER_ANONYMOUS_URLS', [
    {
      name: 'signup',
      url: '/signup/',
      title: 'Регистрация',
      template: 'js/app/site/view/signup.html',
      controller: "Signup"
    }, {
      name: 'signin',
      url: '/signin/',
      title: 'Вход',
      template: 'js/app/site/view/signin.html'
    }
  ]).config(function($routeProvider, CUSTOMER_ANONYMOUS_URLS) {
    return _.map(CUSTOMER_ANONYMOUS_URLS, function(url) {
      return $routeProvider.when(url.url, {
        templateUrl: "" + window.ng_config.static_url + url.template,
        controller: url.controller
      });
    });
  });

}).call(this);
