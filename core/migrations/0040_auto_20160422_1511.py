# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20160422_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='Children',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]