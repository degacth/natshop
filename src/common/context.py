# coding: utf-8
from django.conf import settings
from globals import globals
from catalog.models import Category
from section.models import Section


def set_base_data(request):
    if request.path.startswith('/adm/'): return {}

    return {
        'host': globals.request.get_host(),
        'settings': settings,
        'config': globals.config,
        'category_product': Category.objs.all(),
        'top_menu': Section.get_main_menu(),
    }
