# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=20, verbose_name='编号')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='名称')),
                ('material', models.CharField(blank=True, max_length=20, verbose_name='材质')),
                ('texture', models.CharField(blank=True, max_length=20, verbose_name='纹理')),
                ('width', models.FloatField(blank=True, default=150, verbose_name='幅宽')),
                ('ref_price', models.FloatField(blank=True, default=0, verbose_name='推荐价格')),
                ('is_per_meter', models.BooleanField(default=True, verbose_name='单位')),
                ('used_for', models.CharField(blank=True, max_length=100, verbose_name='用途')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='详细描述')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClothDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='ClothImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='ColorMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_color', models.CharField(max_length=10)),
                ('external_color', models.CharField(max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(help_text='(所在单号)', max_length=20, verbose_name='单号')),
                ('color', models.CharField(max_length=20, verbose_name='颜色')),
                ('price_per_unit', models.FloatField(verbose_name='单价')),
                ('total_units', models.FloatField(help_text='(单位为m或kg)', verbose_name='总米数/克重')),
                ('total_bundles', models.FloatField(blank=True, default=0, verbose_name='总匹数')),
                ('total_price', models.FloatField(verbose_name='总价')),
                ('total_paid', models.FloatField(blank=True, default=0, verbose_name='已付金额')),
                ('is_withdrawn', models.BooleanField(default=False, verbose_name='是否为退单')),
                ('is_warehouse', models.BooleanField(default=False, verbose_name='是否为仓库')),
                ('order_date', models.DateTimeField(verbose_name='下单日期')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth', verbose_name='布料')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.FloatField(verbose_name='米数')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Order', verbose_name='所属订单')),
            ],
        ),
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, help_text='(Different shops which owns the same cloth have different number)', max_length=10)),
                ('price', models.FloatField(blank=True, default=0)),
                ('price_detail', models.CharField(blank=True, max_length=100)),
                ('file_path', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='颜色')),
                ('remain_meter', models.FloatField(verbose_name='剩余米数')),
                ('wastage_meter', models.FloatField(verbose_name='损耗米数')),
                ('put_in_time', models.DateTimeField(verbose_name='入库时间')),
                ('sale_time', models.DateTimeField(blank=True, verbose_name='出库时间')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth', verbose_name='布料')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, max_length=20)),
                ('shop_name', models.CharField(blank=True, max_length=20)),
                ('phone_main', models.CharField(blank=True, max_length=20)),
                ('phone_second', models.CharField(blank=True, max_length=20)),
                ('phone_third', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bank_name_main', models.CharField(blank=True, max_length=20)),
                ('bank_number_main', models.CharField(blank=True, max_length=20)),
                ('bank_name_second', models.CharField(blank=True, max_length=20)),
                ('bank_number_second', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='WholeSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='颜色')),
                ('batch_id', models.CharField(max_length=20, verbose_name='缸号')),
                ('is_in_stock', models.BooleanField(default=True)),
                ('put_in_time', models.DateTimeField(verbose_name='入库时间')),
                ('sale_time', models.DateTimeField(blank=True, verbose_name='出库时间')),
                ('meter', models.FloatField(verbose_name='米数')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Cloth', verbose_name='布料')),
            ],
        ),
        migrations.AddField(
            model_name='ownership',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Shop'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Shop', verbose_name='顾客'),
        ),
        migrations.AddField(
            model_name='colormap',
            name='ownership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Ownership'),
        ),
    ]
