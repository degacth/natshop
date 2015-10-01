angular.module 'ParsersApp', ['xml', 'ngResource']

.constant "YAM_PARSER_API_URL", "#{window.ng_config.api}/parsers/getxml_by_url"


.controller 'LocalCatalogController', ($scope, $http) ->
  _.extend $scope,
    local_catalogs: $http.get('/catalog/yamarket').success (data) -> print data
    log: print


.config (x2jsProvider, $httpProvider) ->
  x2jsProvider.config =
    escapeMode: on

  $httpProvider.interceptors.push 'xmlHttpInterceptor'


.directive 'localCatalog', ->
  templateUrl: '/static/parsers/js/views/local_catalog.html'
  controller: 'LocalCatalogController'


.directive 'childrenCatalog', ->
  scope:
    local_catalogs: '=children'
    log: '='

  templateUrl: '/static/parsers/js/views/local_catalog.html'


print = console.log.bind console
