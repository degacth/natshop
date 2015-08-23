# coding: utf-8

from django.conf.urls import include, url
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from mailer.views import send
from .models import Feedback, FeedbackSerializer
from common.views import recaptcha_verify
from django.utils.translation import ugettext as _


class FeedbackList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        return None
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        verified = recaptcha_verify(request, request.data['captcha'])
        if verified is True:
            self.create(request, *args, **kwargs)

            return Response({
                '_success': _('success submitted feedback')
            }, status=status.HTTP_201_CREATED)

        return Response({
            '_error': _('Unable to validate feedback')
        }, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    url(r'^$', FeedbackList.as_view()),
]