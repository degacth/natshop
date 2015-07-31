# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('value', models.TextField(verbose_name='value', blank=True)),
                ('type', models.CharField(blank=True, max_length=200, verbose_name='type', choices=[(b'integer', 'integer number'), (b'array', 'array_split_comma')])),
            ],
            options={
                'verbose_name': 'config_item',
                'verbose_name_plural': 'config_items',
            },
        ),
    ]
