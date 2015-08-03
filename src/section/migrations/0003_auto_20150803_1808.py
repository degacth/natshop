# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20150802_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='action',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435', blank=True, choices=[(b'', '\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e')]),
        ),
        migrations.AlterField(
            model_name='section',
            name='grouping',
            field=models.CharField(default=b'', max_length=255, verbose_name='grouping', blank=True, choices=[(b'', '\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e'), (b'main_menu', 'main_menu'), (b'main_category', 'main_category')]),
        ),
    ]
