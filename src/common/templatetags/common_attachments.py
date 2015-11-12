# coding: utf-8
from django import template
from django.db.models import QuerySet
from django.db.models.fields.files import ImageFieldFile
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from easy_thumbnails.files import get_thumbnailer
from ..models import Attachment
from catalog.models import Product

register = template.Library()
_getAttrs = lambda attrs: " ".join(map((lambda v: '%s="%s"' % v), attrs))


def _getImage(path, size, only_path, attrs):
    try:
        path = (get_thumbnailer(path).get_thumbnail({'size': size.split('x'), 'crop': True}).url, _getAttrs(attrs))
    except:
        return ""
    if only_path: return path[0]
    return '<img src="%s" %s />' % path

get_image_path = lambda path, size: _getImage(path, size, True, dict())


@register.simple_tag
def get_aimage(obj, size, **kwargs):
    if isinstance(obj, Product) and obj.parse_image:
        return '<div><img src="%s" /></div>' % obj.parse_image

    elif isinstance(obj, ImageFieldFile):
        path = obj

    elif isinstance(obj, Attachment):
        path = obj.file

    elif hasattr(obj, "file"):
        path = obj.file

    else:
        if hasattr(obj, 'attachments'):
            if hasattr(obj.attachments, 'all'): attachments = obj.attachments.all()
            else: attachments = obj.attachments

            images = filter(lambda i: i.status, attachments)
            if len(images):
                path = images[0].file
            else:
                return ""

    only_path = kwargs.get('only_path', False)
    if only_path: del kwargs['only_path']

    return _getImage(path, size, only_path, kwargs.iteritems())


@register.assignment_tag
def get_aimages(obj, size, **kwargs): return filter(lambda item: not item.status, obj.attachments)


@register.simple_tag
def add_attachments(obj):
    if hasattr(obj, 'attachments'): return ""
    try:
        obj.attachments = Attachment.objects.filter(object_id=obj.id,
                                                    content_type=ContentType.objects.get_for_model(obj))

    except AttributeError:
        pass

    return ""
