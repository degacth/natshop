# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20151101_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='parse_url',
            field=models.CharField(default=b'', max_length=255, verbose_name='parse_url', blank=True),
        ),
    ]
