angular.module 'ParsersApp', ['xml', 'ngResource']

.config (x2jsProvider, $httpProvider) ->
  x2jsProvider.config =
    escapeMode: on
  $httpProvider.interceptors.push 'xmlHttpInterceptor'


.factory 'getYamCatalogTree', (CatalogModel) ->
  (catalog_list) ->
    get_model = (xml_model) -> new CatalogModel
      id: xml_model._id
      title: xml_model.__text
      parent_id: xml_model._parentId

    set_children = (catalogs, parent) ->
      return if _.isEmpty catalogs
      parent.children = []
      filtered = _.filter catalogs, (item) ->
        if item._parentId is parent.id then parent.children.push(get_model item) and no else yes
      return if _.isEmpty parent.children
      _.map parent.children, (item) -> set_children filtered, item

    set_children catalog_list, root = {}
    root


.factory 'getYamProducts', (ProductModel) ->
  (product_list) ->
    make_product = (product) -> new ProductModel
      id: product._id
      title: product.name
      available: product._available is "true"
      parent_id: product.categoryId
      currency_id: product.currentcyId
      descritpion: product.descritpion
      image: product.picture
      price: product.price
      url: product.url
      params: _.map product.param, (param) -> { value: param.__text, name: param._name }

    _.map product_list, make_product


.factory 'CatalogModel', ($resource) -> $resource "/url/:id"
.factory 'ProductModel', ($resource) -> $resource "/product/:id"


.directive 'catalogTree', -> templateUrl: '/static/parsers/js/views/local_catalog.html'
.factory 'catalogTreeControllerMixin', ->
  ($scope) ->
    _.extend $scope,
      catalog_selected: (catalog) ->
        $scope.current_catalog = catalog
        $scope.catalog_selected_after?(catalog)
      is_active_catalog: (catalog) -> if catalog is $scope.current_catalog then "uk-active" else ""
