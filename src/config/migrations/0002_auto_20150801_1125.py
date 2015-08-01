# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438', 'verbose_name_plural': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='config',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='config',
            name='type',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0438\u043f', choices=[(b'integer', 'integer number'), (b'array', '\u043c\u0430\u0441\u0441\u0438\u0432, \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e')]),
        ),
        migrations.AlterField(
            model_name='config',
            name='value',
            field=models.TextField(verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435', blank=True),
        ),
    ]
