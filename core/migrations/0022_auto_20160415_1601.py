# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160415_1600'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together=set([('Date', 'Time', 'FieldID')]),
        ),
    ]