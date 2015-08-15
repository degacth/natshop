# coding: utf-8
from toolz.itertoolz import first
from django.conf import settings
from globals import globals
from catalog.models import Category, Product
from section.models import Section


def set_base_data(request):
    path = request.path
    excluded = (
        '/%s' % settings.ADMIN_URL,
        '/%s/' % settings.API_URL.strip('/'),
    )
    if path.startswith(excluded): return {}

    get_array_item_by_name = lambda name, collection: [item for item in collection if item.name == name]
    get_first = lambda collection: first(collection) if len(collection) else None
    get_by_name = lambda name, collection: get_first(get_array_item_by_name(name, collection))

    section_main = Section.get_main()

    return {
        'host': settings.SITE_HOST,
        'settings': settings,
        'config': globals.config,
        'category_product': Category.get_main(),
        'top_menu': section_main,
        'catalog_section': globals.catalog,
        'last_products': get_last_products(request.session),
        'cart_section': get_by_name('shopping-cart', section_main),
    }


def get_last_products(session):
    last_products_id = session.get('last_products', [])
    if not len(last_products_id): return []
    lprods = Product.get_last_products(last_products_id)

    # rearrange products list
    last_products = range(0, len(lprods))
    for prod in lprods:
        index = last_products_id.index(prod.id)
        last_products[index] = prod

    return last_products
