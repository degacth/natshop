# coding: utf-8
from django.views import generic
from django import shortcuts
from django import http
from section import models
from common import views
from catalog.models import Product

class Main(generic.TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        stock = models.Section.objects.get(name='stock')

        return {
            'seo': views.get_seo(),
            'novelty': Product.get_novelty(),
            'about': models.Section.objects.get(name='about'),
            'stock': stock,
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


class Contacts(generic.TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        return views.get_default_context(kwargs['section'])


class SectionArticle(generic.TemplateView):
    template_name = 'section.html'

    def get_context_data(self, **kwargs):
        sec = kwargs['section']

        article_id = kwargs['obj_id'] if kwargs['obj_id'] else None
        if article_id:
            article = shortcuts.get_object_or_404(models.Article, pk=article_id)
        else:
            articles = sec.get_articles()
            if len(articles):
                article = articles[0]
            else:
                raise http.Http404('Не найдена статья')

        return {
            'seo': views.get_seo(article),
            'current': article,
        }


_namedclass = {
    'default': Default.as_view(),
    'contacts': Contacts.as_view(),
    'section_article': SectionArticle.as_view()
}
