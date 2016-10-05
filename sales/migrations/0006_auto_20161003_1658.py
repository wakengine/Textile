# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20161003_1635'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Shop',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='name',
            new_name='own_name',
        ),
        migrations.AddField(
            model_name='goods',
            name='owner',
            field=models.ManyToManyField(to='sales.Shop'),
        ),
    ]
