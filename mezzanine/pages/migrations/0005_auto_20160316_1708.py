# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160316_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='_meta_title_ru',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='page',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='page',
            name='titles_ru',
            field=models.CharField(editable=False, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='richtextpage',
            name='content_ru',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
    ]
