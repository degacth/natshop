# coding: utf-8
from django.views import generic
from django import shortcuts
from django import http
from section import models
from common import views
from catalog.models import Product, Category


class Main(generic.TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        return {
            'seo': views.get_seo(),
            'banner_products': Product.get_banner(),
            'other_products': Product.get_other(),
            'other_stock': Category.get_other(),
        }


class SectionResolver(views.TreeResolver):
    tree_model = models.Section
    root_view = Main.as_view

    @views.TreeResolver.prepare_get
    def get(self, request, **kwargs):
        path = self.tree_path
        section = self.tree_object
        kwargs['section'] = section
        kwargs['path'] = path
        return _namedclass["%s" % section.action](request, **kwargs)


class Default(generic.TemplateView):
    template_name = 'section.html'

    def get_context_data(self, **kwargs):
        return views.get_default_context(kwargs['section'])


_namedclass = {
    'default': Default.as_view(),
}
