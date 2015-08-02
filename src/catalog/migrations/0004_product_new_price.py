# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_in_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(default=0, verbose_name='\u0426\u0435\u043d\u0430', max_digits=11, decimal_places=2),
        ),
    ]
