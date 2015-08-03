# coding: utf-8
from django.db import models
from mptt.models import TreeForeignKey
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common


class SectionManager(common.TextEntityManager): pass


class Section(common.Tree):
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    action = models.CharField(_('action'), max_length=255, default="", blank=True, choices=(
        ('', _('default'),),
    ))
    grouping = models.CharField(_('grouping'), default="", blank=True, max_length=255, choices=(
        ('', _('default'),),
        ('main_menu', _('main_menu')),
        ('main_category', _('main_category')),
    ))

    text_entity_fields = common.TextEntity.text_entity_fields + ['parent', 'name', 'action', 'grouping']

    @classmethod
    def get_main(cls):
        return cls.objs.filter(grouping="main_menu")

    def get_articles(self):
        return Article.objects.filter(parent=self, status=True)

    objs = SectionManager()


class Article(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    short = RichTextField(_('short'))
    parent = TreeForeignKey(Section, verbose_name=_('parent'))
