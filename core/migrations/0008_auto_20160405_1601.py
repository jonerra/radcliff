# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160405_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Date',
            field=models.IntegerField(choices=[(0, ''), (1, '8:00AM - 10:00AM'), (2, '10:00AM - 12:00PM'), (3, '12:00PM - 2:00PM'), (4, '2:00PM - 4:00PM'), (5, '4:00PM - 6:00PM'), (6, '6:00PM - 8:00PM')], default=0, unique=True),
        ),
    ]