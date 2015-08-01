# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150801_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(upload_to=common.models.PathAndRename(b'attachment/product'), verbose_name='image', blank=True),
        ),
    ]
