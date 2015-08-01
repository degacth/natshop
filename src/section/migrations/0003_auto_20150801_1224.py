# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20150801_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.ImageField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='image', blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='file',
            field=models.ImageField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='image', blank=True),
        ),
    ]
