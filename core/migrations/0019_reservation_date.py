# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 22:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_field_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 22, 1, 42, 785160, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
