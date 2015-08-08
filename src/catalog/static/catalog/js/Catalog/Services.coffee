angular.module 'Catalog'

.factory 'Cart', (CATALOG_API_URL, $resource) -> $resource "#{CATALOG_API_URL}/cart/:product", product: "@id"

.service 'Carter', -> class
  constructor: (@cart) ->

  set: (cart_data) ->
    if -1 < index = @get_index cart_data.id then @cart[index].count = cart_data.count
    else @cart.push cart_data

  get_index: (id) ->
    @cart.indexOf _.find @cart, (c) -> c.id is id
