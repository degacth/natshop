# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_product_parse_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='margin',
            field=models.PositiveIntegerField(default=0, verbose_name='margin'),
        ),
    ]
