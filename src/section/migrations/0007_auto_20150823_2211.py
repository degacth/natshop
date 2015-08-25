# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0006_article_other_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short',
            field=ckeditor.fields.RichTextField(verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
