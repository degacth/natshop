# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_auto_20150819_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='other_info',
            field=models.TextField(default=b'', null=True, verbose_name='other_info'),
        ),
    ]
