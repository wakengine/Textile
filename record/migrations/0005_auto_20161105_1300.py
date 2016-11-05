# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 05:00
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('record', '0004_auto_20161104_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='clothcategory',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='clothmaterial',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='clothmaterial',
            name='material',
        ),
        migrations.RemoveField(
            model_name='clothtexture',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='clothtexture',
            name='texture',
        ),
        migrations.AddField(
            model_name='cloth',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='record.CategoryOfCloth'),
        ),
        migrations.AddField(
            model_name='cloth',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='record.MaterialOfCloth'),
        ),
        migrations.AddField(
            model_name='cloth',
            name='texture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='record.TextureOfCloth'),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='breadth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='grams_per_m2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ClothCategory',
        ),
        migrations.DeleteModel(
            name='ClothMaterial',
        ),
        migrations.DeleteModel(
            name='ClothTexture',
        ),
    ]
