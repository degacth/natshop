from rest_framework import serializers
from .models import Product, Catalog


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'get_full_path', 'get_thumbnail_tag', 'get_price']


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'parent', 'title']
