# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='_meta_title_en',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
    ]
