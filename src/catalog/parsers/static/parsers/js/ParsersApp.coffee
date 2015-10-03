angular.module 'ParsersApp', ['xml', 'ngResource']

.config (x2jsProvider, $httpProvider) ->
  x2jsProvider.config =
    escapeMode: on
  $httpProvider.interceptors.push 'xmlHttpInterceptor'


.factory 'getCatalogTree', (CatalogModel) ->
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


.factory 'CatalogModel', ($resource) -> $resource "/url/:id"
.directive 'catalogTree', -> templateUrl: '/static/parsers/js/views/local_catalog.html'
