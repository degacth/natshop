# coding: utf-8

from django.db import models
from mptt.models import TreeForeignKey
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common
from section.models import Section


class Catalog(common.StructuralEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    @classmethod
    def get_top_level(cls): return cls.objects.filter(parent=None, status=True).order_by('-sort')

    def get_full_path(self): return "/catalog%s" % common.StructuralEntity.get_full_path(self)

    def get_products(self): return Product.objects.filter(parent=self, status=True)


class CategoryManager(common.TextEntityManager): pass


class Category(Section):
    objs = CategoryManager()


class Product(common.LeafEntity, common.TextEntity, common.SeoEntity):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    price = models.DecimalField(_('price'), max_digits=11, decimal_places=2, default=0)
    new_price = models.DecimalField(_('new_price'), max_digits=11, decimal_places=2, default=0)
    short = RichTextField(_('short'))
    parent = TreeForeignKey(Catalog, verbose_name=_('parent'))
    category = models.ManyToManyField(Category, blank=True)
    in_banner = models.BooleanField(_('in_banner'), default=False)

    def get_price(self): return self.new_price or self.price

    def get_old_price(self): return self.new_price and self.price

    @common.memoize_field('_categories_css_class')
    def get_categories_css_class(self): return reduce(
        lambda cls, cat: "%s %s" % (cls, cat.name),
        self.category.all(),
        ""
    ).strip()

    @classmethod
    def get_banner(cls): return Product.objs.filter(in_banner=True).select_related()
