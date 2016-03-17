# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields
import mezzanine.shop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160316_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content_ru',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_ru',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_ru',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_ru',
            field=mezzanine.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_ru',
            field=mezzanine.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_ru',
            field=mezzanine.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
    ]
