// Generated by CoffeeScript 1.10.0
(function() {
  var print;

  angular.module('ParsersApp', ['xml', 'ngResource']).constant("YAM_PARSER_API_URL", window.ng_config.api + "/parsers/getxml_by_url").controller('LocalCatalogController', function($scope, $resource) {
    return _.extend($scope, {
      local_catalogs: $resource('/adm/catalog/catalog/tree_json/').query(),
      log: print
    });
  }).config(function(x2jsProvider, $httpProvider) {
    x2jsProvider.config = {
      escapeMode: true
    };
    return $httpProvider.interceptors.push('xmlHttpInterceptor');
  }).directive('localCatalog', function() {
    return {
      templateUrl: '/static/parsers/js/views/local_catalog.html',
      controller: 'LocalCatalogController'
    };
  }).directive('childrenCatalog', function() {
    return {
      scope: {
        local_catalogs: '=children',
        log: '='
      },
      templateUrl: '/static/parsers/js/views/local_catalog.html'
    };
  });

  print = console.log.bind(console);

}).call(this);
