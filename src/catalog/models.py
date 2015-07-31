from django.db import models
from mptt.models import TreeForeignKey
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common
from globals import globals


class Catalog(common.StructuralEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    @classmethod
    def get_top_level(cls):
        return cls.objects.filter(parent=None, status=True).order_by('-sort')

    def get_full_path(self):
        return "/catalog%s" % common.StructuralEntity.get_full_path(self)

    def get_products(self):
        return Product.objects.filter(parent=self, status=True)


class Product(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    price = models.DecimalField(_('price'), max_digits=11, decimal_places=2, default=0)
    short = RichTextField(_('short'))
    parent = TreeForeignKey(Catalog, verbose_name=_('parent'))

    def get_price(self):
        return self.price
