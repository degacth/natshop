# coding: utf-8

from django.contrib import admin
from ..models import Catalog
from .models import YamUrl


class YamParser(Catalog):
    class Meta:
        proxy = True


@admin.register(YamParser)
class YamParserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): return False


@admin.register(YamUrl)
class YamUrlAdmin(admin.ModelAdmin): pass
