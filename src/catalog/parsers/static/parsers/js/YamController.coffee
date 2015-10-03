angular.module 'ParsersApp'


.controller 'YamController', ($scope, $http, getCatalogTree, YAM_PARSER_API_URL) ->
  _.extend $scope,
    url:
      value: 'http://www.nordman.ru/yaget/'

    load: (url) ->
      $http.get "#{YAM_PARSER_API_URL}/#{url}"
      .success (data) ->

  $http.get('/catalog/yamarket').success (data) ->
    $scope.parent_catalog = getCatalogTree data.yml_catalog.shop.categories.category


.constant "YAM_PARSER_API_URL", "#{window.ng_config.api}/parsers/getxml_by_url"
