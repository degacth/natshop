# coding: utf-8
from django.utils.translation import ugettext as _
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from common import models as common
from common import utils
from . import models
from section.admin import SectionAdmin


@admin.register(models.Catalog)
class CatalogAdmin(DjangoMpttAdmin):
    search_fields = models.Catalog.text_search_fields
    fieldsets = (
        (None, {
            'fields': models.Catalog.text_entity_fields + ['parent', 'name', 'margin'],
        }),

        models.Catalog.seo_fieldset,
    )

    readonly_fields = models.Catalog.text_readonly_fields
    prepopulated_fields = {"name": ("title",)}
    list_filter = ['parent']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = models.Product.text_search_fields + ['^parse_url', 'short', 'info',]
    fieldsets = (
        (None, {
            'fields': models.Product.text_entity_fields + ['short', 'price', 'new_price', 'parent', 'category',
                                                           'in_banner'],
        }),

        (_('parse_info'), {
            'fields': ('parse_url', 'parse_image', 'info'),
            'classes': ('grp-collapse grp-closed',),
        }),

        models.Product.seo_fieldset
    )

    readonly_fields = models.Product.text_readonly_fields
    list_filter = ['parent', 'category', 'in_banner']
    inlines = [common.AttachmentInline]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': utils.remove_list([] + models.Category.text_entity_fields,
                                        ['parent', 'file', 'thumbnail_tag', 'created', 'parent']),
        }),

        models.Category.seo_fieldset,
    )


class OrderItemInline(admin.StackedInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = ['sum']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['sum']
    inlines = [OrderItemInline]
