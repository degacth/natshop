# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20150818_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_url',
            field=models.CharField(default=b'', max_length=255, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_group',
            field=models.ForeignKey(verbose_name='shipping_group', to='catalog.ShippingGroup', null=True),
        ),
    ]
