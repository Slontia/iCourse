# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20171030_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='introduce',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='intro',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
