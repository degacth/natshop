angular.module "Customer"

.controller "CustomerBase", ($scope, $location, CUSTOMER_ANONYMOUS_URLS) ->
  angular.extend $scope,
    anonymous_urls: CUSTOMER_ANONYMOUS_URLS
    get_sidebar: -> "#{window.ng_config.static_url}js/app/site/view/anonymous.html"
    is_active_menu: (path) -> 'active' if $location.path() is path


.controller "Signup", ($scope, CustomerModel) ->
  angular.extend $scope,
    info:
      name: 'Дегтярёв Александр Сергеевич'
      email: 'degacth@yandex.ru'
      password: '123'
    repeat_password: '123'

    check_form: -> @signup_form.$valid and @info.password is @repeat_password

    save: ->
      return unless @check_form()
      customer = new CustomerModel @info
      do customer.$save

print = console.log.bind console
