# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-18 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170118_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_time',
            name='master',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='landing.Master'),
            preserve_default=False,
        ),
    ]
