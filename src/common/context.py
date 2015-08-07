# coding: utf-8
from django.conf import settings
from globals import globals
from catalog.models import Category, Product
from section.models import Section


def set_base_data(request):
    if request.path.startswith('/%s' % settings.ADMIN_URL): return {}

    return {
        'host': settings.SITE_HOST,
        'settings': settings,
        'config': globals.config,
        'category_product': Category.get_main(),
        'top_menu': Section.get_main(),
        'catalog_section': globals.catalog,
        'last_products': get_last_products(request.session)
    }


def get_last_products(session):
    last_products_id = session.get('last_products', [])
    lprods = Product.get_last_products(last_products_id)

    # rearrange products list
    last_products = range(0, len(lprods))
    for prod in lprods:
        index = last_products_id.index(prod.id)
        last_products[index] = prod

    return last_products
