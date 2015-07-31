# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

config_types = {
    'array': {
        'title': _('array_split_comma'),
        'cb': lambda v: v.strip(',').split(','),
    },

    'integer': {
        'title': _('integer number'),
        'cb': lambda v: int(v)
    },
}

config_types_choices = lambda: map(
    lambda k: (k, config_types[k]['title']),
    config_types
)


def init_config():
    config = dict()
    for v in Config.objects.all():
        config[v.name] = v.value if not v.type in config_types else config_types[v.type]['cb'](v.value)

    return config


class Config(models.Model):
    title = models.CharField(_('title'), max_length=255)
    name = models.CharField(_('name'), max_length=255)
    value = models.TextField(_('value'), blank=True)
    type = models.CharField(_('type'), max_length=200, choices=config_types_choices(), blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('config_item')
        verbose_name_plural = _('config_items')
