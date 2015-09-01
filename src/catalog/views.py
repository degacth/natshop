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
        if not len(catalog.get_subs()): return self.product_list(context, **kwargs)

        context['catalog_list'] = catalog.get_subs()
        return context

    def product_list(self, context, catalog, **kwargs):
        self.template_name = "products.html"
        context['products'] = views.get_paginator(catalog.get_products())
        return context


class Product(generic.TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        id = kwargs['obj_id']
        product = models.Product.objects.get(pk=id)

        # update last_products
        session = kwargs['session']
        last_products_id = session.get('last_products', [])
        session['last_products'] = []
        if not id in last_products_id: last_products_id.insert(0, product.id)
        session['last_products'] = last_products_id[:6]
        return get_default_context(product)


class ProductCategory(generic.TemplateView):
    template_name = 'product_category.html'

    def get_context_data(self, **kwargs):
        section = kwargs['section']
        context = views.get_default_context(section)
        context['products'] = views.get_paginator(models.Product.get_by_category_name(section.name))
        return context



def get_default_context(catalog=None):
    add_root = None
    if not catalog:
        catalog = globals.catalog
    else:
        add_root = globals.catalog

    return {
        'seo': views.get_seo(catalog, add_root),
        'current': catalog,
        'catalog_menu': models.Catalog.get_top_level(),
    }
