# coding: utf-8

from django.contrib import admin
from ..models import Catalog


class YamParser(Catalog):
    class Meta:
        proxy = True


@admin.register(YamParser)
class YamParserAdmin(admin.ModelAdmin): pass
