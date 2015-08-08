angular.module 'Site'

.controller 'Base', ($scope, Cart) ->
  angular.extend $scope,
    cart_model: Cart
    cart: Cart.query()
