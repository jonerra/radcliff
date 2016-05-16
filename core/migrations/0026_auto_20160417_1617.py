# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 16:17
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20160416_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='PhoneNumber',
        ),
        migrations.AddField(
            model_name='player',
            name='PhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number'),
        ),
    ]
