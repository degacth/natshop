# coding: utf-8
from django.conf import settings
from section.models import Section
from catalog.models import Catalog
from globals import globals


def set_base_data(request):
    return {
        'host': globals.request.get_host(),
        'main_menu': Section.get_main(),
        'catalog_menu': Catalog.get_top_level(),
        'settings': settings,
        'config': globals.config,
    }
