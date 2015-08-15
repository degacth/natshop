# coding: utf-8

from django.conf.urls import include, url
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from .models import Customer, CustomerSerializer
from mailer.views import send


class CustomerView(APIView):
    def get(self, request):
        customer = self.request.customer
        if not customer: return Response()
        return Response(CustomerSerializer(customer).data)

    def post(self, request):
        data = request.data
        email = Customer.objects.normalize_email(data['email'])
        customer = request.customer

        # Data update
        if customer:
            if email != customer.email:
                try:
                    Customer.objects.get(email=email)
                    return self._registered_error()

                except Customer.DoesNotExist:
                    customer.email = email

            customer.phone = data['phone']
            customer.name = data['name']
            customer.save()

            return self._success_saved(customer, u"Данные успешно обновлены")

        # Signup
        try:
            Customer.objects.get(email=email)
            return self._registered_error()

        except Customer.DoesNotExist:
            customer = Customer(**{
                'name': data['name'],
                'email': email,
            })

            customer.set_password(data['password'])
            customer.save()
            customer.activate(request.session)

            return self._success_saved(customer, u"Спасибо за регистрацию")

    def _registered_error(self):
        return Response({
            '_error': u"Пользователь с указанным email уже зарегистрирован",
        }, status=status.HTTP_400_BAD_REQUEST)

    def _success_saved(self, customer, message):
        response = CustomerSerializer(customer).data
        response['_success'] = message
        return Response(response, status=status.HTTP_201_CREATED)


class CustomerLogin(APIView):
    def post(self, request):
        data = request.data
        email = Customer.objects.normalize_email(data['email'])
        try:
            customer = Customer.objects.get(email=email)
            if customer.check_password(data['password']):
                customer.activate(request.session)
                return Response(CustomerSerializer(customer).data, status=status.HTTP_202_ACCEPTED)
        except Customer.DoesNotExist:
            pass

        return Response({
            '_error': 'Неверно введён логин или пароль',
        }, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        request.session[Customer.SESSION_KEY] = None
        return Response()


class ForgetView(APIView):
    def post(self, request):
        data = request.data
        email = Customer.objects.normalize_email(data['email'])

        try:
            customer = Customer.objects.get(email=email)
            password = Customer.objects.make_random_password()
            customer.set_password(password)

            try:
                send(u'Изменение пароля для пользователя %s' % customer.name, u'''
                    Ваш новый пароль: %s <br />
                    Используйте этот адрес электронной почты в качестве логина
                ''' % password, [email])

                customer.save()

            except:
                return Response({
                    '_error': 'Не удалось отправить письмо, попробуйте позже, возможно почтовый сервер недоступен'
                }, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Customer.DoesNotExist:
            pass

        return Response({'_success': 'На указанный адрес выслан новый пароль'})


urlpatterns = [
    url(r'^$', CustomerView.as_view()),
    url(r'^login$', CustomerLogin.as_view()),
    url(r'^forget$', ForgetView.as_view()),
]
