# coding: utf-8
import os
import datetime
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField
from easy_thumbnails.files import get_thumbnailer


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = "%s/%s/%s" % (
            sub_path.strip('/'),
            datetime.date.today().year,
            datetime.date.today().month,
        )

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class ThumbnailMixin(object):
    def thumbnail_tag(self):
        return '<img src="%s" />' % get_thumbnailer(self.file).get_thumbnail({'size': (160, 160), 'crop': True}).url

    thumbnail_tag.short_description = _('preview')
    thumbnail_tag.allow_tags = True


pather = PathAndRename('attachment/files')


class Attachment(models.Model, ThumbnailMixin):
    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

    file = models.FileField(_('file'), upload_to=pather)
    comment = models.TextField(_('comment'), null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    status = models.BooleanField(_('status'), default=True)

    def __unicode__(self):
        return self.thumbnail_tag()


class AttachmentInline(GenericTabularInline):
    model = Attachment
    extra = 0
    fields = ('file', 'comment', 'thumbnail_tag', 'status')
    readonly_fields = ('thumbnail_tag',)


class TextEntityManager(models.Manager):
    def get_queryset(self):
        return super(TextEntityManager, self).get_queryset().filter(status=True).order_by('-sort')


class TextEntity(models.Model, ThumbnailMixin):
    class Meta:
        abstract = True
        ordering = ['-sort']

    title = models.CharField(_('title'), max_length=255)
    description = RichTextField(_('description'), blank=True, null=True, default="")
    file = models.ImageField(_('image'), upload_to=pather, blank=True)
    status = models.BooleanField(_('status'), default=True)
    sort = models.IntegerField(_('sort'), default=0)
    created = models.DateField(_('created'), default=timezone.now)

    def __unicode__(self):
        return self.title

    text_entity_fields = [
        'title', 'file', 'thumbnail_tag', 'status', 'sort', 'created', 'description',
    ]

    text_search_fields = ['title', 'description']
    text_readonly_fields = ['thumbnail_tag']


class SeoEntity(models.Model):
    class Meta:
        abstract = True

    seo_title = models.CharField(_('seo title'), max_length=255, null=True, blank=True)
    seo_description = models.TextField(_('seo description'), null=True, blank=True)
    seo_keywords = models.TextField(_('seo keywords'), null=True, blank=True)

    seo_fieldset = ('SEO', {
        'fields': ('seo_title', 'seo_description', 'seo_keywords'),
        'classes': ('grp-collapse grp-closed',),
    })


class StructuralEntity(MPTTModel):
    class Meta:
        abstract = True
        ordering = ['-sort']

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.SlugField(_('name'), max_length=255, unique=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, verbose_name=_('parent'))

    def get_full_path(self):
        parents = []
        parents_path = "/"
        if hasattr(self, 'get_ancestors'):
            for parent in self.get_ancestors():
                parents.append(parent.name)

        if len(parents): parents_path += '/'.join(parents) + '/'

        return "%s%s/" % (parents_path, self.name)


class Tree(StructuralEntity, TextEntity, SeoEntity):
    objects = models.Manager()
    objs = TextEntityManager()


class LeafEntity(models.Model):
    class Meta:
        abstract = True

    def get_full_path(self):
        return "%s%d" % (self.parent.get_full_path(), self.id)
