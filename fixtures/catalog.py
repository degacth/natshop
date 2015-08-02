# coding: utf-8

import init
import fake
from catalog.models import Catalog, Category, Product

Catalog.objects.all().delete()
Category.objects.all().delete()

for i in xrange(1, 6):
    catalog = Catalog.objects.create(**{
        'title': 'Каталог номер%s' % i,
        'name': 'catalog%s' %i,
        'file': fake.get_file(),
    })

    for j in xrange(1, 8):
        sub_catalog = Catalog.objects.create(**{
            'title': 'Подраздел%s' % j,
            'name': 'subcat%s%s' % (i, j),
            'parent': catalog,
            'file': fake.get_file(),
        })

for name in ['hits', 'novelty', 'best_price']:
    category = Category.objects.create(**{
        'title': name.capitalize(),
        'name': name,
    })
