# coding: utf-8
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

register.inclusion_tag('catalog/tags/product_image_wrapper.html', name='product_image')(
    lambda product, size: {'product': product, 'size': size})


@register.filter
def price(value): return mark_safe(
    '{:20,.2f}'.format(value).replace(',', ' ') + ' <i class="uk-icon-rub"></i>'
)
