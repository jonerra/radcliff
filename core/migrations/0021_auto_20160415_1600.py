# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20160414_2226'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together=set([('Date', 'Time')]),
        ),
    ]