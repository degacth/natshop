from django.forms import widgets
from rest_framework import serializers
from . import models


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ['id', 'username', 'email', 'phone', 'message']
