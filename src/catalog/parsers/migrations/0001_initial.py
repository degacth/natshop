# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20150827_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='YamUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255, verbose_name='url')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
            options={
                'verbose_name': 'yam_url',
                'verbose_name_plural': 'yam_urls',
            },
        ),
        migrations.CreateModel(
            name='YamParser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.catalog',),
        ),
    ]
