# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 02:33
from __future__ import unicode_literals

import asks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asks', '0003_auto_20170723_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='file_sender',
            field=models.FileField(null=True, upload_to=asks.models.upload_location),
        ),
        migrations.AddField(
            model_name='ask',
            name='file_staff',
            field=models.FileField(null=True, upload_to=asks.models.upload_location),
        ),
        migrations.AddField(
            model_name='ask',
            name='height_field_image',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ask',
            name='image_sender',
            field=models.ImageField(height_field='height_field_image', null=True, upload_to=asks.models.upload_location, width_field='width_field_image'),
        ),
        migrations.AddField(
            model_name='ask',
            name='image_staff',
            field=models.ImageField(height_field='height_field_image', null=True, upload_to=asks.models.upload_location, width_field='width_field_image'),
        ),
        migrations.AddField(
            model_name='ask',
            name='width_field_image',
            field=models.IntegerField(default=0),
        ),
    ]
