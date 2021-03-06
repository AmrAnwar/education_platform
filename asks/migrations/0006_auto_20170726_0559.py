# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:59
from __future__ import unicode_literals

import asks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asks', '0005_auto_20170726_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='image_sender',
            field=models.ImageField(blank=True, height_field='height_field_image', null=True, upload_to=asks.models.upload_location, width_field='width_field_image'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='image_staff',
            field=models.ImageField(blank=True, height_field='height_field_image', null=True, upload_to=asks.models.upload_location, width_field='width_field_image'),
        ),
    ]
