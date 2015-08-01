# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b', 'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='parent',
            field=mptt.fields.TreeForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', to='section.Section'),
        ),
        migrations.AlterField(
            model_name='article',
            name='seo_description',
            field=models.TextField(null=True, verbose_name='SEO \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='seo_keywords',
            field=models.TextField(null=True, verbose_name='SEO \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='seo_title',
            field=models.CharField(max_length=255, null=True, verbose_name='SEO \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='short',
            field=ckeditor.fields.RichTextField(verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='section',
            name='action',
            field=models.CharField(default=b'Default', max_length=255, verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435', choices=[(b'default', '\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e'), (b'contacts', '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'), (b'section_article', 'section_article')]),
        ),
        migrations.AlterField(
            model_name='section',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='in_menu',
            field=models.BooleanField(default=False, verbose_name='\u0412 \u043c\u0435\u043d\u044e'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.SlugField(unique=True, max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='section',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', blank=True, to='section.Section', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='seo_description',
            field=models.TextField(null=True, verbose_name='SEO \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='seo_keywords',
            field=models.TextField(null=True, verbose_name='SEO \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='seo_title',
            field=models.CharField(max_length=255, null=True, verbose_name='SEO \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='section',
            name='status',
            field=models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
