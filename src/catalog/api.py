# coding: utf-8

import re
from django.conf.urls import include, url
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from catalog.models import Product, Order, OrderItem, OrderSerializer, Catalog
from common.templatetags.common_attachments import get_image_path
from .serializer import ProductSerializer, CatalogSerializer


class Cart(APIView):
    _get_cart_index = lambda self, cart, id: cart.index(*([item for item in cart if item['id'] == id] or None))

    def get(self, request, **kwargs):
        # self._set_cart([])
        return Response(self._get_cart())

    def post(self, request, product):
        return Response(self._add_cart())

    def delete(self, request, product):
        cart = self._get_cart()
        index = self._get_cart_index(cart, int(product))
        cart.remove(cart[index])

        self._set_cart(cart)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_cart(self):
        return self.request.session.get('cart', [])

    def _clear_cart(self):
        self.request.session['cart'] = []

    def _set_cart(self, cart):
        self.request.session['cart'] = cart

    def _add_cart(self):
        data = self.request.data
        cart = self._get_cart()
        product = Product.objs.select_related().get(pk=data['id'])
        data['price'] = float(product.get_price())
        data['image'] = get_image_path(product.file, '320x320')
        data['title'] = product.title
        data['url'] = product.get_full_path()

        try:
            index = self._get_cart_index(cart, data['id'])
            cart[index] = data
        except TypeError:
            cart.append(data)

        self._set_cart(cart)
        return data


class OrderView(Cart, APIView):
    def get(self, request, **kwargs):
        customer = request.customer
        orders = OrderSerializer(Order.objects.filter(customer=customer), many=True)
        return Response(data=orders.data)

    def post(self, request):
        data = request.data
        customer = request.customer
        if not customer: return self._order_error("Отсутствуют данные пользователя")

        cart = self._get_cart()
        if not len(cart): return self._order_error("Отсутствуют данные выбранных товаров")

        order = Order(comment=data['comment'], customer=customer)
        order.save()

        map(lambda item: OrderItem.objects.create(**{
            'title': item['title'],
            'comment': item.get('comment', ""),
            'count': item['count'],
            'price': item['price'],
            'product_url': item['url'],
            'order': order,
        }), cart)

        self._clear_cart()

        return Response({
            '_success': "Заказ сделан успешно"
        }, status=status.HTTP_201_CREATED)

    def _order_error(self, error_string, status_data=status.HTTP_400_BAD_REQUEST):
        return Response({
            '_error': error_string
        }, status=status_data)


class LastProducts(APIView):
    def get(self, request):
        last_products_id = request.session.get('last_products', [])
        if not len(last_products_id): return Response([])

        products = Product.get_last_products(last_products_id)
        return Response(ProductSerializer(products, many=True).data)


class CatalogView(APIView):
    def get(self, request, **kwargs):
        return Response(CatalogSerializer(Catalog.objs.all(), many=True).data)


class ProductView(APIView):
    def post(self, request, **kwargs):
        data = request.data
        if data.get('password', '') != settings.PARSE_PASSWORD: return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        Product.objs.create(**{
            'title': data['title'],
            'short': data.get('short', ''),
            'parse_image': data['image'],
            'parse_url': data['parse_url'],
            'parse_link': data.get('link', ''),
            'info': data.get('info', ''),
            'price': get_number_or_0(data['price']),
            'parent_id': int(data['parent']),
        })
        return Response()


get_number = lambda s: re.sub(r'^\s*(\d+).*\s*', '\\1', s)


def get_number_or_0(s):
    try:
        return int(get_number(s))
    except ValueError:
        return 0


urlpatterns = [
    url(r'^cart/(?P<product>\d+)$', Cart.as_view()),
    url(r'^catalog/(?P<catalog>\d*)$', CatalogView.as_view()),
    url(r'^product/(?P<catalog>\d*)$', ProductView.as_view()),
    url(r'^cart$', Cart.as_view()),
    url(r'^order$', OrderView.as_view()),
    url(r'^last_products$', LastProducts.as_view()),
]
