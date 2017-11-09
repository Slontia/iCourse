# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_ipvisitinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipvisitinfo',
            name='first_date',
        ),
        migrations.AddField(
            model_name='ipvisitinfo',
            name='early_date',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ipvisitinfo',
            name='latest_date',
            field=models.CharField(max_length=20),
        ),
    ]
