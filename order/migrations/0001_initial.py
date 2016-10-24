# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 15:19
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=20)),
                ('internal_id', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('price_per_unit', models.FloatField()),
                ('total_units', models.FloatField()),
                ('total_bundles', models.FloatField(blank=True, default=0)),
                ('total_price', models.FloatField()),
                ('is_not_paid', models.BooleanField(default=False)),
                ('is_withdrawn', models.BooleanField(default=False)),
                ('is_warehouse', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('order_date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.Cloth')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
