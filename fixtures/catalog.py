# coding: utf-8

import init
import fake
from catalog.models import Catalog, CategoryProduct, Product

catalogs = []
for i in xrange(1, 6):
    catalog = Catalog(title="Каталог номер%s" % i, name="cat%s" % i)
