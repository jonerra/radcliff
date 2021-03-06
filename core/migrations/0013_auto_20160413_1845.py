# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160408_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='GuardianFirstName',
        ),
        migrations.AddField(
            model_name='player',
            name='GuardianFirstName',
            field=models.CharField(max_length=300, verbose_name='Guardian First Name'),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='Children',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Children',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='Returning',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Returning',
            field=models.IntegerField(choices=[(0, ''), (1, 'Yes'), (2, 'No')], default=0),
        ),
    ]
