# coding: utf-8
from django.conf import settings
from globals import globals
from catalog.models import Category
from section.models import Section


def set_base_data(request):
    if request.path.startswith('/%s' % settings.ADMIN_URL): return {}

    return {
        'host': settings.SITE_HOST,
        'settings': settings,
        'config': globals.config,
        'category_product': Category.get_main(),
        'top_menu': Section.get_main(),
        'catalog_section': globals.catalog
    }
