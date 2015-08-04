# coding: utf-8

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from mptt.models import TreeForeignKey
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common
from section.models import Section
from globals import globals


class CatalogManager(common.TextEntityManager): pass


class Catalog(common.StructuralEntity, common.TextEntity, common.SeoEntity, common.FullPathMixin):
    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    full_path_prefix = "/catalog"
    objects = models.Manager()
    objs = CatalogManager()

    @classmethod
    def get_top_level(cls): return cls.objs.filter(parent=None)

    def is_active_path(self): return globals.request.path.startswith(self.get_full_path())

    def get_products(self): return Product.objects.filter(parent=self, status=True)

    @common.memoize_field('_subs')
    def get_subs(self): return CatalogManager.query_wrapper(self.get_children())


receiver(post_save, sender=Catalog)(common.make_full_path_signal)


class CategoryManager(common.TextEntityManager): pass


class Category(Section):
    objs = CategoryManager()

    @classmethod
    def get_main(cls):
        return cls.objs.filter(grouping="main_category")

    @classmethod
    def get_other(cls):
        return cls.objs.filter(grouping="")


receiver(post_save, sender=Category)(common.make_full_path_signal)


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

    @classmethod
    def select_prefetch_related(cls, queryset): return queryset.select_related().prefetch_related('category')

    @classmethod
    def get_banner(cls): return cls.select_prefetch_related(cls.objs.filter(in_banner=True))

    @classmethod
    def get_other(cls): return cls.select_prefetch_related(
        cls.objs.filter(category__in=Category.get_other()).distinct())
