# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20160415_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='DateOfBirth',
        ),
        migrations.AddField(
            model_name='player',
            name='DateOfBirth',
            field=models.DateField(verbose_name='Date Of Birth'),
        ),
        migrations.RemoveField(
            model_name='player',
            name='Zipcode',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='DateOfBirth',
            field=models.DateField(verbose_name='Date Of Birth'),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='Zipcode',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Zipcode',
            field=models.IntegerField(verbose_name='Zip Code'),
        ),
    ]
