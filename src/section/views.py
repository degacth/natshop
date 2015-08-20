# coding: utf-8
from django.http import Http404
from django.views import generic
from django import shortcuts
from django import http
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
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

        action = "%s" % section.action
        if _namedclass.get(action, False): return _namedclass[action](request, **kwargs)

        try:
            template_name = "%s.html" % section.name
            get_template(template_name)
            kwargs['template_name'] = template_name
            return TemplateByName.as_view()(request, **kwargs)

        except TemplateDoesNotExist: pass

        raise Http404()


class Default(generic.TemplateView):
    template_name = 'section.html'

    def get_context_data(self, **kwargs):
        return views.get_default_context(kwargs['section'])


class TemplateByName(generic.TemplateView):
    def get_context_data(self, **kwargs):
        self.template_name = kwargs['template_name']
        return views.get_default_context(kwargs['section'])


_namedclass = {
    'default': Default.as_view(),
}
