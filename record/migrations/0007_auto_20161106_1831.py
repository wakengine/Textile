# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('record', '0006_auto_20161105_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscontactimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothinshopimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entityimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entitypaymentimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderimage',
            name='thumbnail',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
