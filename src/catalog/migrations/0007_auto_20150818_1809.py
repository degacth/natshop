# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150813_2015'),
        ('catalog', '0006_catalog_full_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', choices=[(0, 'new')])),
                ('comment', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('customer', models.ForeignKey(verbose_name='customer', to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('comment', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('count', models.PositiveSmallIntegerField(verbose_name='count')),
                ('price', models.DecimalField(default=0, verbose_name='\u0426\u0435\u043d\u0430', max_digits=11, decimal_places=2)),
                ('order', models.ForeignKey(verbose_name='order', to='catalog.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='shipping_group',
            field=models.ForeignKey(verbose_name='shipping_group', to='catalog.ShippingGroup'),
        ),
    ]
