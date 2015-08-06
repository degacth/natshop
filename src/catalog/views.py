# coding: utf-8

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.views import generic
from common import views
from globals import globals
from section.models import Section
from . import models


class RootView(generic.TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = get_default_context()
        context['catalog_list'] = context['catalog_menu']
        return context


class CatalogResolver(views.TreeResolver):
    tree_model = models.Catalog
    root_view = RootView.as_view

    @views.TreeResolver.prepare_get
    def get(self, request, **kwargs):
        kwargs["catalog"] = self.tree_object
        if kwargs['obj_id']: return Product.as_view()(request, **kwargs)
        kwargs["page"] = request.GET.get('page')
        return Catalog.as_view()(request, **kwargs)


class Catalog(generic.TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        catalog = kwargs['catalog']
        context = get_default_context(catalog)

        if not len(catalog.get_subs()):
            self.template_name = "products.html"
            context['products'] = catalog.get_products()
            return context

        context['catalog_list'] = catalog.get_subs()
        return context
        product_paginator = Paginator(catalog.get_products_descendants(), globals.config['items_per_page'])
        page = kwargs['page']
        try:
            products = product_paginator.page(page)
        except PageNotAnInteger:
            products = product_paginator.page(1)
        except EmptyPage:
            products = product_paginator.page(product_paginator.num_pages)

        context = views.get_default_context(catalog)
        context['products'] = products
        context['catalog_descendants'] = catalog.get_descendants()
        return context


class Product(generic.TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        product = models.Product.objects.get(pk=kwargs['obj_id'])

        last_products_id = kwargs['session'].get('last_products', [])
        kwargs['session']['last_products'] = []
        __last_products = models.Product.get_last_products(last_products_id)

        # rearrange products list
        prod_len = min(len(last_products_id), len(__last_products))
        last_products = range(0, prod_len)
        for prod in __last_products:
            index = last_products_id.index(prod.id)
            last_products[index] = prod
        # update last_products
        if not product.id in last_products_id: last_products_id.insert(0, product.id)
        kwargs['session']['last_products'] = last_products_id[:4]

        context = views.get_default_context(product)
        context.update({
            'product': product,
            'similar': product.get_similar(),
            'last_products': last_products,
        })

        return context


def get_default_context(catalog=None):
    add_root = None
    if not catalog: catalog = globals.catalog
    else: add_root = globals.catalog

    return {
        'seo': views.get_seo(catalog, add_root),
        'current': catalog,
        'catalog_menu': models.Catalog.get_top_level(),
    }
