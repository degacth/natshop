angular.module 'Catalog'


.controller "Product", ($scope, Carter) ->
  carter = new Carter($scope.cart)
  cart = $scope.cart

  angular.extend $scope,
    id: null
    add_cart: ->
      new $scope.cart_model
        id: @id
        count: 1

      .$save().then (data) ->
        carter.set(data)
        $scope.in_cart = yes

  $scope.$watch cart, ->
    cart.$promise.then ->
      $scope.in_cart = -1 < carter.get_index $scope.id


.controller "Cart", ($scope) ->
  angular.extend $scope,
    sum: -> _.reduce (_.map $scope.cart, (c) -> c.price * c.count), (l, n) -> l + n


.controller "MainProducts", ($scope) ->
  angular.extend $scope,
    category: null
    is_hidden: (id, categories...) -> ! (@category in categories)
    is_active: (id) -> 'active' if id is @category


print = console.log.bind console
