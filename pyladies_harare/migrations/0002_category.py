# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyladies_harare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('shortdesc', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
