from django.http import HttpResponseBadRequest
from rest_framework import mixins
from rest_framework import generics
from . import models
from . import serializers
from common import views


class FeedbackList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        verified = views.recaptcha_verify(request, request.data['captcha'])
        if verified is True:
            return self.create(request, *args, **kwargs)

        return HttpResponseBadRequest(verified)
