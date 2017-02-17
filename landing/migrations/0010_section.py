# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20170217_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='section', verbose_name='Изображение')),
                ('content', models.TextField(verbose_name='Содержимое раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
    ]
