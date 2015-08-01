# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': '\u043e\u0442\u043a\u043b\u0438\u043a', 'verbose_name_plural': '\u043e\u0442\u043a\u043b\u0438\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='admin_message',
            field=models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='adminname',
            field=models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='answer_date',
            field=models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u0432\u0435\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='\u043d\u043e\u0432\u044b\u0439'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='is_notified',
            field=models.BooleanField(default=False, verbose_name='\u043e\u043f\u043e\u0432\u0435\u0449\u0451\u043d'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.BooleanField(default=False, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='username',
            field=models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f'),
        ),
    ]
