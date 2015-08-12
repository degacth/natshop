angular.module "Customer", ['ngResource', 'ngRoute']

.constant 'CUSTOMER_ANONYMOUS_URLS', [
  name: 'signup'
  url: '/signup/'
  title: 'Регистрация'
  template: 'js/app/site/view/signup.html'
  controller: "Signup"
,
  name: 'signin'
  url: '/signin/'
  title: 'Вход'
  template: 'js/app/site/view/signin.html'
]

.config ($routeProvider, CUSTOMER_ANONYMOUS_URLS) ->
  _.map CUSTOMER_ANONYMOUS_URLS, (url) ->
    $routeProvider.when url.url,
      templateUrl: "#{ window.ng_config.static_url }#{ url.template }"
      controller: url.controller
