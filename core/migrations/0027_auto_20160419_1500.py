# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20160417_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='FieldID',
        ),
        migrations.AddField(
            model_name='reservation',
            name='FieldID',
            field=models.ForeignKey(on_delete='id', to='core.Field'),
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='VolunteerID',
        ),
        migrations.AddField(
            model_name='reservation',
            name='VolunteerID',
            field=models.ForeignKey(on_delete='id', to='core.Volunteer'),
        ),
    ]
