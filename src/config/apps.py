# config: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConfigConfig(AppConfig):
    name = 'config'
    verbose_name = _('Config')
