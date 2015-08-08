angular.module 'Catalog'

.factory 'Cart', (CATALOG_API_URL, $resource) -> $resource "#{CATALOG_API_URL}/cart/:product_id/:count"
