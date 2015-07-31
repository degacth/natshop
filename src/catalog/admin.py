# coding: utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from common import models as common
from . import models


@admin.register(models.Catalog)
class CatalogAdmin(DjangoMpttAdmin):
    search_fields = common.text_search_fields
    fieldsets = (
        (None, {
            'fields': ('title', 'name', 'parent', 'sort', 'status', 'description',),
        }),

        common.seo_fieldset,
    )

    prepopulated_fields = {"name": ("title",)}
    list_filter = ['parent']
    inlines = [common.AttachmentInline]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = common.text_search_fields
    fieldsets = (
        (None, {
            'fields': (
                'title', 'price', 'parent', 'status', 'created', 'short', 'description'),
        }),

        common.seo_fieldset,
    )

    list_filter = ['parent']
    inlines = [common.AttachmentInline]
