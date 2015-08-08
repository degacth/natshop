from toolz.itertoolz import first
from django.conf.urls import include, url
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from catalog.models import Product


class Cart(APIView):
    _get_cart_index = lambda self, cart, id: cart.index(*([item for item in cart if item['id'] == id] or None))

    def get(self, request, **kwargs):
        # self._set_cart([])
        return Response(self._get_cart())

    def post(self, request, product):
        return Response(self._add_cart())

    def delete(self, request):
        pass

    def _get_cart(self):
        return self.request.session.get('cart', [])

    def _set_cart(self, cart):
        self.request.session['cart'] = cart

    def _add_cart(self):
        data = self.request.data
        cart = self._get_cart()
        product = Product.objs.get(pk=data['id'])
        data['price'] = float(product.get_price())

        try:
            index = self._get_cart_index(cart, data['id'])
            cart[index] = data
        except TypeError:
            cart.append(data)

        self._set_cart(cart)
        return data


urlpatterns = [
    url(r'^cart/(?P<product>\d+)$', Cart.as_view()),
    url(r'^cart$', Cart.as_view()),
]
