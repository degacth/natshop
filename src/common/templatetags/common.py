# coding: utf-8
from django import template
from django.conf import locale
from globals import globals

register = template.Library()


@register.filter
def active_path_class(cls, path): return cls if globals.request.path.startswith(path) else ""


@register.filter
def equals_path_class(cls, path): return cls if globals.request.path == path else ""
