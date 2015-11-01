# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20150827_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name='admin_info', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='parse_url',
            field=models.CharField(default=b'', max_length=255, verbose_name='parse_url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
