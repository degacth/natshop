# coding: utf-8
from django import template
from django.conf import locale
from django.core.urlresolvers import reverse
from globals import globals

register = template.Library()


@register.filter
def active_path_class(cls, path): return cls if globals.request.path.startswith(path) else ""


@register.filter
def equals_path_class(cls, path): return cls if globals.request.path == path else ""


@register.simple_tag
def admin_edit(obj):
    app, model = (obj._meta.app_label, obj._meta.model_name,)
    if globals.request.user.is_authenticated():
        return '<a href="%s" target="_blank"><i class="uk-icon-edit"></i></a>' % \
               reverse("admin:%s_%s_change" % (app, model), args=(obj.id,))
    return ""
