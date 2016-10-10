# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothdetail',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='clothimage',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='colormap',
            name='ownership',
        ),
        migrations.RemoveField(
            model_name='ownership',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='ownership',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='retail',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='shopdetail',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='shopimage',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='wholesale',
            name='cloth',
        ),
        migrations.RenameField(
            model_name='orderimage',
            old_name='file_path',
            new_name='img_path',
        ),
        migrations.AlterField(
            model_name='order',
            name='cloth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Cloth', verbose_name='布料'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Shop', verbose_name='顾客'),
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
        migrations.DeleteModel(
            name='ClothDetail',
        ),
        migrations.DeleteModel(
            name='ClothImage',
        ),
        migrations.DeleteModel(
            name='ColorMap',
        ),
        migrations.DeleteModel(
            name='Ownership',
        ),
        migrations.DeleteModel(
            name='Retail',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='ShopDetail',
        ),
        migrations.DeleteModel(
            name='ShopImage',
        ),
        migrations.DeleteModel(
            name='WholeSale',
        ),
    ]
