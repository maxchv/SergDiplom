# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_work_time_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='master',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
