# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255, verbose_name='username')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('message', models.TextField(verbose_name='message_text')),
                ('phone', models.CharField(max_length=255, verbose_name='phone_number')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('adminname', models.CharField(max_length=255, verbose_name='adminname', blank=True)),
                ('admin_message', models.TextField(verbose_name='admin_message', blank=True)),
                ('answer_date', models.DateTimeField(null=True, verbose_name='answer_date', blank=True)),
                ('is_new', models.BooleanField(default=True, verbose_name='is_new')),
                ('is_notified', models.BooleanField(default=False, verbose_name='is_notified')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
    ]
