# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20150818_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='comment',
            field=models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_group',
            field=models.ForeignKey(verbose_name='shipping_group', blank=True, to='catalog.ShippingGroup', null=True),
        ),
    ]
