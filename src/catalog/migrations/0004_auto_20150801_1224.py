# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='file',
            field=models.ImageField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.ImageField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='image', blank=True),
        ),
    ]
