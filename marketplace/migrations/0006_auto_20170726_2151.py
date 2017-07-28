# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20170726_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='course_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='posts',
            name='type',
            field=models.CharField(choices=[('new', 'Brand new'), ('used', 'Second hand'), ('damage', 'Damaged')], default='acads', max_length=8),
        ),
        migrations.AlterField(
            model_name='posts',
            name='condition',
            field=models.CharField(choices=[('new', 'Brand new'), ('used', 'Second hand'), ('damage', 'Damaged')], default='new', max_length=11),
        ),
    ]