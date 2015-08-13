# coding: utf-8

from django.conf.urls import include, url
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from .models import Customer, CustomerSerializer


class CustomerView(APIView):
    def get(self, request):
        customer = self.request.customer
        if not customer: return Response()
        return Response(CustomerSerializer(customer).data)

    def post(self, request):
        data = request.data
        email = Customer.objects.normalize_email(data['email'])
        try:
            Customer.objects.get(email=email)

            return Response({
                '_error': u"Пользователь с указанным email уже зарегистрирован",
            }, status=status.HTTP_400_BAD_REQUEST)

        except Customer.DoesNotExist:
            customer = Customer(**{
                'name': data['name'],
                'email': email,
            })

            customer.set_password(data['password'])
            customer.save()
            customer.activate(request.session)

            response = CustomerSerializer(customer).data
            response['_success'] = u"Спасибо за регистрацию"
            return Response(response, status=status.HTTP_201_CREATED)


urlpatterns = [
    url(r'^$', CustomerView.as_view()),
]
