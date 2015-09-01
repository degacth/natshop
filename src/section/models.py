# coding: utf-8
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.contenttypes import fields
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
        ('blog', _('blog'),),
        ('product_category', _('product_category'),),
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

    @common.memoize_field('_articles')
    def get_articles(self):
        return Article.objs.filter(parent=self).prefetch_related('attachments').select_related()

    objs = SectionManager()


receiver(post_save, sender=Section)(common.make_full_path_signal)


class Article(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    short = RichTextField(_('short'), blank=True)
    parent = TreeForeignKey(Section, verbose_name=_('parent'))
    other_info = models.TextField(_('other_info'), null=True, default="")

    attachments = fields.GenericRelation(common.Attachment, content_type_field='content_type',
                                         object_id_field='object_id')

    def get_attachments(self): return list(self.attachments.all())
