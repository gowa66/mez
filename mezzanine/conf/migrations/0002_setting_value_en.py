# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='value_en',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]