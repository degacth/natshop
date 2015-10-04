# coding: utf-8

from django.db import models
from django.utils.translation import ugettext as _


class YamUrl(models.Model):
    class Meta:
        verbose_name = _('yam_url')
        verbose_name_plural = _('yam_urls')

    url = models.URLField(_('url'), max_length=255)
    title = models.CharField(_('title'), max_length=255)

    def __unicode__(self): return self.title
