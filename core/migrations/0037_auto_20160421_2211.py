# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20160421_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='Picture',
            field=models.ImageField(default='images', null=True, upload_to='images'),
        ),
    ]
