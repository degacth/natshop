# coding: utf-8
from django.conf import settings
from globals import globals


def set_base_data(request):
    return {
        'host': globals.request.get_host(),
        'settings': settings,
        'config': globals.config,
    }
