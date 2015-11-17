# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_catalog_margin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parse_link',
            field=models.CharField(default=b'', max_length=255, verbose_name='parse_link', blank=True),
        ),
    ]
