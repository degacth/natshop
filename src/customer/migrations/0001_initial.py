# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435, \u0435\u0441\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0434\u043e\u043b\u0436\u0435\u043d \u0441\u0447\u0438\u0442\u0430\u0442\u044c\u0441\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u043c. \u0423\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u0442\u0443 \u043e\u0442\u043c\u0435\u0442\u043a\u0443 \u0432\u043c\u0435\u0441\u0442\u043e \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0443\u0447\u0451\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438.', verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0434\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customer',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
