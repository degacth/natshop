# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20150802_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='full_path',
            field=models.CharField(max_length=255, null=True, verbose_name='full_path'),
        ),
    ]
