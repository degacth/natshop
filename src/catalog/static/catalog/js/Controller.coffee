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
    sum: -> cart_sum $scope.cart


.controller "MainProducts", ($scope) ->
  angular.extend $scope,
    category: null
    is_hidden: (id, categories...) -> !(@category in categories)
    is_active: (id) -> 'active' if id is @category


.controller "BasketBase", ($scope, $location, Order, BASKET_URL) ->
  angular.extend $scope,
    order:
      comment: ""

    make_order: ->
      order = new Order @order
      order.$save().then -> $scope.cart.splice 0, $scope.cart.length

  # root url
  $location.path BASKET_URL
  # no root url
  $scope.$on '$locationChangeStart', (e, nw, old) -> unless nw.split('#')[1] then e.preventDefault()


.controller "Basket", ($scope, Carter) ->
  carter = new Carter($scope.cart)

  angular.extend $scope,
    add: (product) ->
      product.count++
      @save product

    sub: (product) ->
      return if product.count <= 1
      product.count--
      @save product

    save: (product) ->
      new @cart_model(product)
      .$save()

    remove: (product) -> product.$delete().then -> carter.remove product

    sum: -> cart_sum $scope.cart

    all_count: -> _.reduce @cart, ((l, n) -> l + n.count), 0


.controller "LastProducts", ($scope, LastProducts) -> $scope.last_products = do LastProducts.query


print = console.log.bind console
cart_sum = (cart) -> _.reduce ( _.map cart, (c) -> c.price * c.count ), ( (l, n) -> l + n ), 0
