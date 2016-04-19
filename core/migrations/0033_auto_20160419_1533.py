# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20160419_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='PhoneNumber',
            field=models.CharField(help_text='Please use the following format: <em>XXX-XXX-XXXX</em>.', max_length=50, verbose_name='Phone Number'),
        ),
    ]