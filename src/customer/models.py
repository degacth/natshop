# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils import six, timezone
from django.utils.translation import ugettext as _
from rest_framework import serializers


class Customer(AbstractBaseUser):
    name = models.CharField(_('name'), max_length=255, blank=True)
    email = models.EmailField(_('email'), blank=True)
    phone = models.CharField(_('phone'), max_length=255, blank=True, default="")
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    SESSION_KEY = 'customer'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customer')

    def activate(self, session):
        session[self.SESSION_KEY] = self.id


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']
