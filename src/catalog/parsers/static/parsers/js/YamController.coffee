angular.module "ParsersApp"


.controller "YamController", ($scope, $http, getCatalogTree, YAM_PARSER_API_URL) ->
  _.extend $scope,
    url:
      value: 'http://www.nordman.ru/yaget/'

    load: (url) ->
      $http.get "#{YAM_PARSER_API_URL}/#{url}"
      .success (data) -> set_yacatalog_data $scope, data, getCatalogTree

.controller "LocalCatalogs", ($scope, $http, getCatalogTree) ->
  $http.get('/catalog/yamarket').success (data) -> set_yacatalog_data $scope, data, getCatalogTree


.constant "YAM_PARSER_API_URL", "#{window.ng_config.api}/parsers/getxml_by_url"


set_yacatalog_data = (scope, xmljson, catalogTreeMaker) ->
  shop = xmljson.yml_catalog.shop
  _.extend scope,
    parent_catalog: catalogTreeMaker shop.categories.category
    site_name: shop.name
    site_url: shop.url
