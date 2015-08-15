angular.module "Customer"

.controller "CustomerBase", ($scope, $location, CUSTOMER_ANONYMOUS_URLS, CUSTOMER_URLS) ->
  angular.extend $scope,
    get_urls: -> if @customer.email then CUSTOMER_URLS else CUSTOMER_ANONYMOUS_URLS
    get_sidebar: -> "#{window.ng_config.static_url}js/app/site/view/customer_menu.html"
    is_active_menu: (path) -> 'active' if $location.path() is path


.controller "Signup", ($scope, $location, CustomerModel, CUSTOMER_URLS) ->
  angular.extend $scope,
    info: {}
    check_form: -> @signup_form.$valid and @info.password is @repeat_password
    save: ->
      return unless @check_form()
      customer = new CustomerModel @info
      customer.$save().then (data) ->
        angular.extend $scope.customer, data
        $location.path get_url_by_name(CUSTOMER_URLS, 'orders').url


.controller "Logout", ($scope, $location, LoginResource, CUSTOMER_ANONYMOUS_URLS) ->
  $scope.logout = -> (new LoginResource()).$delete().then ->
    $scope.customer.email = null
    $location.path get_url_by_name(CUSTOMER_ANONYMOUS_URLS, 'signin').url


.controller "Signin", ($scope, $location, LoginResource, CUSTOMER_URLS, CUSTOMER_ANONYMOUS_URLS) ->
  angular.extend $scope,
    signin: ->
      (new LoginResource(@info)).$save().then (data) ->
        angular.extend $scope.customer, data
        $location.path get_url_by_name(CUSTOMER_URLS, 'orders').url

    get_anonymous_url_by_name: _.partial get_url_by_name, CUSTOMER_ANONYMOUS_URLS


.controller "ForgetPassword", ($scope, ForgetResource) ->
  $scope.forget_resource = new ForgetResource()


get_url_by_name = (collection, name) ->
  print name
  _.find collection, (url) -> url.name is name
print = console.log.bind console
