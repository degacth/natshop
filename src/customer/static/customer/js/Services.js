// Generated by CoffeeScript 1.9.2
(function() {
  angular.module("Customer").factory("CustomerModel", function($resource, CUSTOMER_API_URL) {
    return $resource(CUSTOMER_API_URL + "/", {}, {}, {
      stripTrailingSlashes: false
    });
  }).factory("LoginResource", function($resource, CUSTOMER_API_URL) {
    return $resource(CUSTOMER_API_URL + "/login");
  }).factory("ForgetResource", function($resource, CUSTOMER_API_URL) {
    return $resource(CUSTOMER_API_URL + "/forget");
  });

}).call(this);
