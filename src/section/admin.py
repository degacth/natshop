# coding: utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from common import models as common
import models


@admin.register(models.Section)
class SectionAdmin(DjangoMpttAdmin):
    search_fields = common.text_search_fields
    fieldsets = (
        (None, {
            'fields': ('title', 'name', 'parent', 'action', 'sort', 'status', 'description',),
        }),

        common.seo_fieldset,
    )

    prepopulated_fields = {"name": ("title",)}
    list_filter = ['parent']
    inlines = [common.AttachmentInline]


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = common.text_search_fields
    fieldsets = (
        (None, {
            'fields': ('title', 'parent', 'status', 'created', 'short', 'description'),
        }),

        common.seo_fieldset,
    )

    list_filter = ['parent']
    inlines = [common.AttachmentInline]
