# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-31 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_extenduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='department',
            new_name='position',
        ),
    ]
