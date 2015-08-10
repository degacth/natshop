angular.module 'Catalog', ['ngResource', 'ngRoute']

.constant 'CATALOG_API_URL', "#{window.ng_config.api}/catalog"
.constant 'BASKET_URL', '/basket/'

.config ($routeProvider, BASKET_URL) ->
  $routeProvider
  .when BASKET_URL,
    templateUrl: "#{window.ng_config.static_url}js/app/site/view/basket.html"
    controller: "Basket"

.filter "my_currency", ($filter) -> (num) ->
  "#{num}".replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 ")
