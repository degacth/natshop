angular.module "Customer", ['ngResource', 'ngRoute']

.constant 'CUSTOMER_API_URL', "#{window.ng_config.api}/customer"

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

.constant 'CUSTOMER_URLS', [
  name: 'orders'
  url: '/orders/'
  title: 'Заказы'
  template: 'js/app/site/view/orders.html'
  controller: "Orders"
,
  name: 'info'
  url: '/info/'
  title: 'Личные данные'
  template: 'js/app/site/view/customer_info.html'
,
  name: 'logout'
  url: '/logout/'
  title: 'Выход'
  template: 'js/app/site/view/logout.html'
]

.config ($routeProvider, CUSTOMER_ANONYMOUS_URLS, CUSTOMER_URLS) ->
  _.map [].concat(CUSTOMER_ANONYMOUS_URLS).concat(CUSTOMER_URLS), (url) ->
    $routeProvider.when url.url,
      templateUrl: "#{ window.ng_config.static_url }#{ url.template }"
      controller: url.controller
