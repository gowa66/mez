# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0002_setting_value_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='value_ru',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
