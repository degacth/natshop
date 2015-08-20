# coding: utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from common import models as common
import models


@admin.register(models.Section)
class SectionAdmin(DjangoMpttAdmin):
    search_fields = models.Section.text_search_fields
    fieldsets = (
        (None, {
            'fields': models.Section.text_entity_fields,
        }),

        models.Section.seo_fieldset,
    )

    readonly_fields = models.Section.text_readonly_fields
    prepopulated_fields = {"name": ("title",)}
    list_filter = ['parent']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = models.Article.text_search_fields
    fieldsets = (
        (None, {
            'fields': ('title', ('parent', 'status', 'created'), 'short', 'description', 'other_info'),
        }),

        models.Article.seo_fieldset,
    )

    list_filter = ['parent']
    inlines = [common.AttachmentInline]
