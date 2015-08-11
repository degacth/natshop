angular.module "Customer", ['ngResource', 'ngRoute']

.constant 'SIGNIN_URL', '/signin/'
.constant 'SIGNUP_URL', '/signup/'

.config ($routeProvider, SIGNIN_URL, SIGNUP_URL) ->
  $routeProvider
  .when SIGNUP_URL,
    templateUrl: "#{window.ng_config.static_url}js/app/site/view/signup.html"
