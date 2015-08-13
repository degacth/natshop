angular.module 'Site'

.controller 'Base', ($scope, Cart, CustomerModel) ->
  angular.extend $scope,
    cart_model: Cart
    cart: Cart.query()
    customer: CustomerModel.get()
