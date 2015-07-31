# coding: utf-8
from django.db import models
from mptt.models import TreeForeignKey
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common

_defaultActions = (
    ('default', _('default'),),
    ('contacts', _('contacts'),),
    ('section_article', _('section_article'),),
)

getActions = lambda: _defaultActions


class Section(common.StructuralEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    action = models.CharField(
        _('action'), max_length=255, default='Default',
        choices=getActions()
    )
    in_menu = models.BooleanField(_('in menu'), default=False)

    @classmethod
    def get_main(self):
        return Section.objects.filter(in_menu=True)

    def get_articles(self):
        return Article.objects.filter(parent=self, status=True)


class Article(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    short = RichTextField(_('short'))
    parent = TreeForeignKey(Section, verbose_name=_('parent'))
