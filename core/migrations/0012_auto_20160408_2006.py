# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20160407_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='Returning',
            field=models.IntegerField(choices=[(0, ''), (1, 'Y'), (2, 'N')], default=0),
        ),
    ]
