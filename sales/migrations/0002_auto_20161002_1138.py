# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='mobile',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agency',
            name='telephone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
