# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_auto_20160111_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='uname',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
