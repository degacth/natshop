angular.module "Customer"

.controller "CustomerBase", ($scope, $location) ->
  angular.extend $scope,
    get_sidebar: -> "#{window.ng_config.static_url}js/app/site/view/anonymous.html"
    is_active_menu: (path) -> 'active' if $location.path() is path

print = console.log.bind console
