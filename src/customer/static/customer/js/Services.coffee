angular.module "Customer"

.factory "CustomerModel", ($resource, CUSTOMER_API_URL) ->
  $resource "#{CUSTOMER_API_URL}/", {}, {}, stripTrailingSlashes: off

.factory "LoginResource", ($resource, CUSTOMER_API_URL) -> $resource "#{CUSTOMER_API_URL}/login"
