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


class SectionManager(common.TextEntityManager): pass


class Section(common.Tree):
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    action = models.CharField(
        _('action'), max_length=255, default='Default',
        choices=getActions()
    )
    in_menu = models.BooleanField(_('in menu'), default=False)

    text_entity_fields = common.TextEntity.text_entity_fields + ['parent', 'name', 'action', 'in_menu']

    @classmethod
    def get_main_menu(cls):
        return cls.objs.filter(in_menu=True)

    def get_articles(self):
        return Article.objects.filter(parent=self, status=True)

    objs = SectionManager()


class Article(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    short = RichTextField(_('short'))
    parent = TreeForeignKey(Section, verbose_name=_('parent'))
