# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433', 'verbose_name_plural': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '\u0442\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='description',
            field=ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.SlugField(unique=True, max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', blank=True, to='catalog.Catalog', null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='seo_description',
            field=models.TextField(null=True, verbose_name='SEO \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='seo_keywords',
            field=models.TextField(null=True, verbose_name='SEO \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='seo_title',
            field=models.CharField(max_length=255, null=True, verbose_name='SEO \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='status',
            field=models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=mptt.fields.TreeForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', to='catalog.Catalog'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, verbose_name='\u0426\u0435\u043d\u0430', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_description',
            field=models.TextField(null=True, verbose_name='SEO \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_keywords',
            field=models.TextField(null=True, verbose_name='SEO \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_title',
            field=models.CharField(max_length=255, null=True, verbose_name='SEO \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='short',
            field=ckeditor.fields.RichTextField(verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, to='catalog.CategoryProduct', null=True),
        ),
    ]
