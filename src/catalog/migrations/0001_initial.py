# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('sort', models.IntegerField(default=0, verbose_name='sort')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='created')),
                ('seo_title', models.CharField(max_length=255, null=True, verbose_name='seo title', blank=True)),
                ('seo_description', models.TextField(null=True, verbose_name='seo description', blank=True)),
                ('seo_keywords', models.TextField(null=True, verbose_name='seo keywords', blank=True)),
                ('name', models.SlugField(unique=True, max_length=255, verbose_name='name')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent', blank=True, to='catalog.Catalog', null=True)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='description', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('sort', models.IntegerField(default=0, verbose_name='sort')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='created')),
                ('seo_title', models.CharField(max_length=255, null=True, verbose_name='seo title', blank=True)),
                ('seo_description', models.TextField(null=True, verbose_name='seo description', blank=True)),
                ('seo_keywords', models.TextField(null=True, verbose_name='seo keywords', blank=True)),
                ('price', models.DecimalField(default=0, verbose_name='price', max_digits=11, decimal_places=2)),
                ('short', ckeditor.fields.RichTextField(verbose_name='short')),
                ('parent', mptt.fields.TreeForeignKey(verbose_name='parent', to='catalog.Catalog')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
