angular.module 'Catalog', ['ngResource', 'ngRoute']

.constant 'CATALOG_API_URL', "#{window.ng_config.api}/catalog"
.constant 'BASKET_URL', '/basket/'

.config ($routeProvider, BASKET_URL) ->
  $routeProvider
  .when BASKET_URL,
    templateUrl: "#{window.ng_config.static_url}js/app/site/view/basket.html"
    controller: "Basket"

.filter "rub", ($filter, $sce) -> (num) -> $sce.trustAsHtml "#{fix2 num}".replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1 ") + P


P = ' <i class="uk-icon-rub"></i> '
int = parseInt
fix2 = (num) -> int(num).toFixed 2
print = console.log.bind console
