# coding: utf-8
from django import template
from django.conf import locale

register = template.Library()

@register.simple_tag
def is_active_menu(path, name):
    delim = '/'
    path = path.strip(delim).split(delim)
    return 'active' if path[0] == name else ""

@register.filter
def price(value):
    return '{:20,.2f}'.format(value).replace(',', ' ') + ' P'
