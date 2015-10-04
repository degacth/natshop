// Generated by CoffeeScript 1.10.0
(function() {
  var set_yacatalog_data;

  angular.module("ParsersApp").controller("YamController", function($scope) {
    return _.log;
  }).controller("LocalCatalogs", function($scope, $http, getCatalogTree, catalogTreeControllerMixin) {
    catalogTreeControllerMixin($scope);
    return $http.get('/catalog/yamarket').success(function(data) {
      return set_yacatalog_data($scope, data, getCatalogTree);
    });
  }).controller("ParsedCatalogs", function($scope, $http, getCatalogTree, YAM_PARSER_API_URL, catalogTreeControllerMixin) {
    catalogTreeControllerMixin($scope);
    return _.extend($scope, {
      url: {
        value: 'http://www.nordman.ru/yaget/'
      },
      load: function(url) {
        return $http.get(YAM_PARSER_API_URL + "/" + url).success(function(data) {
          return set_yacatalog_data($scope, data, getCatalogTree);
        });
      }
    });
  }).constant("YAM_PARSER_API_URL", window.ng_config.api + "/parsers/getxml_by_url");

  set_yacatalog_data = function(scope, xmljson, catalogTreeMaker) {
    var shop;
    shop = xmljson.yml_catalog.shop;
    return _.extend(scope, {
      parent_catalog: catalogTreeMaker(shop.categories.category),
      site_name: shop.name,
      site_url: shop.url
    });
  };

}).call(this);
