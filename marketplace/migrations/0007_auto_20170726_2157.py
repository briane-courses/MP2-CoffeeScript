# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_auto_20170726_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='type',
            field=models.CharField(choices=[('acads', 'Academic'), ('office', 'Office')], default='acads', max_length=8),
        ),
    ]