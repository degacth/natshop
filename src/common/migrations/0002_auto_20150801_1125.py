# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': '\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b', 'verbose_name_plural': '\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='comment',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='\u0444\u0430\u0439\u043b'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='status',
            field=models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
    ]
