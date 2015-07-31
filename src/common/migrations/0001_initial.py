# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='file')),
                ('comment', models.TextField(null=True, verbose_name='comment', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
    ]
