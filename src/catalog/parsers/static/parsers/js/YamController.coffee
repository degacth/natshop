angular.module 'ParsersApp'


.controller 'YamController', ($scope, $http, YAM_PARSER_API_URL) ->
  _.extend $scope,
    url:
      value: 'http://www.nordman.ru/yaget/'

    load: (url) ->
      $http.get "#{YAM_PARSER_API_URL}/#{url}"
      .success (data) ->
        print data

print = console.log.bind console
