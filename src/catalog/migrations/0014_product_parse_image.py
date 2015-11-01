# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20151101_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parse_image',
            field=models.CharField(default=b'', max_length=255, verbose_name='parse_image', blank=True),
        ),
    ]
