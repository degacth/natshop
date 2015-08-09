// Generated by CoffeeScript 1.9.2
(function() {
  var print,
    slice = [].slice,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  angular.module('Catalog').controller("Product", function($scope, Carter) {
    var cart, carter;
    carter = new Carter($scope.cart);
    cart = $scope.cart;
    angular.extend($scope, {
      id: null,
      add_cart: function() {
        return new $scope.cart_model({
          id: this.id,
          count: 1
        }).$save().then(function(data) {
          carter.set(data);
          return $scope.in_cart = true;
        });
      }
    });
    return $scope.$watch(cart, function() {
      return cart.$promise.then(function() {
        return $scope.in_cart = -1 < carter.get_index($scope.id);
      });
    });
  }).controller("Cart", function($scope) {
    return angular.extend($scope, {
      sum: function() {
        return _.reduce(_.map($scope.cart, function(c) {
          return c.price * c.count;
        }), function(l, n) {
          return l + n;
        });
      }
    });
  }).controller("MainProducts", function($scope) {
    return angular.extend($scope, {
      category: null,
      is_hidden: function() {
        var categories, id, ref;
        id = arguments[0], categories = 2 <= arguments.length ? slice.call(arguments, 1) : [];
        return !(ref = this.category, indexOf.call(categories, ref) >= 0);
      },
      is_active: function(id) {
        if (id === this.category) {
          return 'active';
        }
      }
    });
  });

  print = console.log.bind(console);

}).call(this);
