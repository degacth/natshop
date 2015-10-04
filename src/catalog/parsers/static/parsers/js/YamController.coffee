angular.module "ParsersApp"


.controller "YamController", ($scope) ->
  _.extend $scope,
    all_products: {}


.controller "LocalCatalogs", ($scope, $http, getYamCatalogTree, getYamProducts, catalogTreeControllerMixin) ->
  catalogTreeControllerMixin $scope
  $http.get('/catalog/yamarket').success (data) -> set_yacatalog_data $scope, data, getYamCatalogTree, getYamProducts


.controller "ParsedCatalogs", ($scope, $http, getYamCatalogTree, getYamProducts,YAM_PARSER_API_URL, catalogTreeControllerMixin) ->
  catalogTreeControllerMixin $scope
  update_catalog_tree = (data_promise) ->
    data_promise.success (data) -> set_yacatalog_data $scope, data, getYamCatalogTree, getYamProducts

  get_xml_json = _.memoize (url) -> $http.get "#{YAM_PARSER_API_URL}/#{url}"

  _.extend $scope,
    load: (url) -> url and update_catalog_tree get_xml_json url
    catalog_selected_after: (catalog) -> $scope.all_products.parsed = _.filter $scope.products, (product) -> product.parent_id is catalog.id


.constant "YAM_PARSER_API_URL", "#{window.ng_config.api}/parsers/getxml_by_url"


set_yacatalog_data = (scope, xmljson, catalogTreeMaker, productsMaker) ->
  shop = xmljson.yml_catalog.shop
  _.extend scope,
    parent_catalog: catalogTreeMaker shop.categories.category
    site_name: shop.name
    site_url: shop.url
    products: productsMaker shop.offers?.offer
