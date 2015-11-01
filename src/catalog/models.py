# coding: utf-8

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from mptt.models import TreeForeignKey
from rest_framework import serializers
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from common import models as common
from section.models import Section
from customer.models import Customer
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
    def get_top_level(cls):
        return cls.objs.filter(parent=None)

    def is_active_path(self):
        return globals.request.path.startswith(self.get_full_path())

    @common.memoize_field('_products')
    def get_products(self):
        return Product.objs.filter(parent=self).select_related('parent').prefetch_related('category')

    @common.memoize_field('_subs')
    def get_subs(self):
        return CatalogManager.query_wrapper(self.get_children())

    def get_catalog_tiles(self):
        max_len = 4
        tiles = []
        subs = CatalogManager.query_wrapper(self.get_children()).order_by('?')[:max_len]
        if subs: tiles = tiles + list(subs)

        tiles_len = len(tiles)
        if tiles_len >= max_len: return tiles

        return tiles + list(self.get_products().order_by('?')[:max_len - tiles_len])


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
    short = RichTextField(_('short'), blank=True, default='')
    parent = TreeForeignKey(Catalog, verbose_name=_('parent'))
    category = models.ManyToManyField(Category, blank=True)
    in_banner = models.BooleanField(_('in_banner'), default=False)
    info = RichTextField(_('admin_info'), blank=True, default='')
    parse_url = models.CharField(_('parse_url'), max_length=255, default='')

    def get_price(self): return self.new_price or self.price

    def get_old_price(self): return self.new_price and self.price

    @classmethod
    def select_prefetch_related(cls, queryset): return queryset.select_related().prefetch_related('category')

    @classmethod
    def get_banner(cls): return cls.select_prefetch_related(cls.objs.filter(in_banner=True))

    @classmethod
    def get_other(cls): return cls.select_prefetch_related(
        cls.objs.filter(category__in=Category.get_other()).distinct())

    @classmethod
    def get_last_products(cls, ids): return cls.objs.filter(id__in=ids).select_related('parent')

    def get_category_comma_ids(self):
        ids = ",".join(map(lambda category: str(category.id), self.category.all()))
        return ", %s" % ids if ids else ""

    @classmethod
    def get_by_category_name(cls, name):
        return cls.select_prefetch_related(cls.objs.filter(category=Category.objs.get(name=name)))


class OrderManager(models.Manager):
    def get_queryset(self):
        return super(OrderManager, self).get_queryset().order_by('-created', '-id')


class Order(models.Model):
    class Meta: pass

    statuses = (
        (0, _('new')),
    )

    objects = OrderManager()

    created = models.DateTimeField(_('created'), default=timezone.now)
    customer = models.ForeignKey(Customer, verbose_name=_('customer'))
    status = models.PositiveSmallIntegerField(_('status'), default=0, choices=statuses)
    comment = models.TextField(_('comment'), blank=True)

    def __unicode__(self): return "# %s %s" % (self.id, self.customer.name)

    def sum(self): return reduce(lambda last, item: last + item.price * item.count, self.orderitem_set.all(), 0)

    @common.memoize_field('_items')
    def get_items(self): return OrderItem.objects.filter(order=self)

    def items(self): return OrderItemSerializer(self.get_items(), many=True).data

    def get_full_sum(self): return reduce(lambda memo, item: item.price * item.count + memo, self.get_items(), 0)


class ShippingGroup(models.Model):
    title = models.CharField(_('title'), max_length=255)


class OrderItem(models.Model):
    title = models.CharField(_('title'), max_length=255)
    comment = models.TextField(_('comment'), blank=True)
    count = models.PositiveSmallIntegerField(_('count'))
    price = models.DecimalField(_('price'), max_digits=11, decimal_places=2, default=0)
    order = models.ForeignKey(Order, verbose_name=_('order'))
    product_url = models.CharField(_('url'), max_length=255, default="")
    shipping_group = models.ForeignKey(ShippingGroup, verbose_name=_('shipping_group'), blank=True, null=True)

    def __unicode__(self): return self.title

    def sum(self): return self.price * self.count if self.count else 0


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['title', 'comment', 'count', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created', 'comment', 'items', 'get_full_sum']
