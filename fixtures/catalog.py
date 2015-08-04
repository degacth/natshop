# coding: utf-8

import init
import fake
from catalog.models import Catalog, Category, Product

Catalog.objects.all().delete()
Category.objects.all().delete()

for i in xrange(1, 6):
    catalog = Catalog.objects.create(**{
        'title': 'Каталог номер%s' % i,
        'name': 'catalog%s' % i,
        'file': fake.get_file(),
    })

    for j in xrange(1, 8):
        sub_catalog = Catalog.objects.create(**{
            'title': 'Подраздел%s' % j,
            'name': 'subcat%s%s' % (i, j),
            'parent': catalog,
            'file': fake.get_file(),
        })

categories = ['hits', 'novelty', 'best_price']
cat_len = len(categories) - 1
for i, name in enumerate(categories):
    category = Category.objects.create(**{
        'title': name.capitalize(),
        'name': name,
        'grouping': 'main_category' if i < cat_len else "",
    })

for i in xrange(1, 40): Product.objects.create(**{
    'title': 'Товар очередной %s' % i,
    'short': fake.lorem,
    'description': fake.lorem * 4,
    'file': fake.get_file(),
    'parent': sub_catalog,
    'price': i * 100,
})

rand_products = lambda limit=10: Product.objs.all().order_by('?')[:limit]

for product in rand_products():
    product.in_banner = True
    product.save()

for category in Category.objs.all():
    for product in rand_products():
        product.category.add(category)
