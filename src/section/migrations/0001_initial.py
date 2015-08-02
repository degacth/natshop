# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import mptt.fields
import common.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', ckeditor.fields.RichTextField(default=b'', null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('file', models.ImageField(upload_to=common.models.PathAndRename(b'attachment/files'), verbose_name='image', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441')),
                ('sort', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('seo_title', models.CharField(max_length=255, null=True, verbose_name='SEO \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('seo_description', models.TextField(null=True, verbose_name='SEO \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('seo_keywords', models.TextField(null=True, verbose_name='SEO \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True)),
                ('short', ckeditor.fields.RichTextField(verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model, common.models.ThumbnailMixin),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('tree_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Tree')),
                ('action', models.CharField(default=b'Default', max_length=255, verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435', choices=[(b'default', '\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e'), (b'contacts', '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'), (b'section_article', 'section_article')])),
                ('in_menu', models.BooleanField(default=False, verbose_name='\u0412 \u043c\u0435\u043d\u044e')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
            bases=('common.tree',),
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=mptt.fields.TreeForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', to='section.Section'),
        ),
    ]
