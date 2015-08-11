# coding: utf-8

from django.views import generic
from section.models import Section
from common.views import get_default_context

class DefaultView(generic.TemplateView):
    template_name = 'customer.html'

    def get_context_data(self, **kwargs):
        section = Section(**{
            'title': u'Кабинет клиента',
        })

        return get_default_context(section)
