# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='in_menu',
        ),
        migrations.AddField(
            model_name='section',
            name='grouping',
            field=models.CharField(default=b'', max_length=255, verbose_name='grouping', choices=[(b'main_menu', 'main_menu')]),
        ),
    ]
