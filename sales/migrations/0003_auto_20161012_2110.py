# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20161012_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.AddField(
            model_name='order',
            name='is_not_paid',
            field=models.BooleanField(default=True, verbose_name='付清'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_warehouse',
            field=models.BooleanField(default=False, verbose_name='仓库'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_withdrawn',
            field=models.BooleanField(default=False, verbose_name='退单'),
        ),
    ]