# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='full_path',
            field=models.CharField(max_length=255, null=True, verbose_name='full_path'),
        ),
    ]
