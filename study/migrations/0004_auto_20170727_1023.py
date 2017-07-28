# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20170727_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='test',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
