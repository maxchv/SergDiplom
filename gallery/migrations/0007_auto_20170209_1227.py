# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20170209_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=150, verbose_name='Краткое описание'),
        ),
    ]
