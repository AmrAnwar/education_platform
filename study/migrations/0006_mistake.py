# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20170727_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('replace', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test_Mistake', to='study.Test')),
            ],
        ),
    ]
