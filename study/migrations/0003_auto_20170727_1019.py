# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20170723_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice_one', models.CharField(max_length=50)),
                ('choice_two', models.CharField(max_length=50)),
                ('choice_three', models.CharField(max_length=50)),
                ('answer', models.CharField(choices=[('a', 'first'), ('b', 'second'), ('c', 'third')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='word',
            name='translation',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='test',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_part', to='study.Part'),
        ),
        migrations.AddField(
            model_name='choices',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test', to='study.Test'),
        ),
    ]
