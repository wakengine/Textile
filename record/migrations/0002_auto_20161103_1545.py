# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='EntityContactMethod',
            new_name='BusinessContactInfo',
        ),
        migrations.RenameModel(
            old_name='BusinessContactMethod',
            new_name='EntityContactInfo',
        ),
        migrations.RemoveField(
            model_name='unitofclothconversion',
            name='unit_from',
        ),
        migrations.RemoveField(
            model_name='unitofclothconversion',
            name='unit_to',
        ),
        migrations.RenameField(
            model_name='businesscontactinfo',
            old_name='contact_method',
            new_name='contact_info',
        ),
        migrations.RenameField(
            model_name='entitycontactinfo',
            old_name='contact_method',
            new_name='contact_info',
        ),
        migrations.RemoveField(
            model_name='businesscontactinfo',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='entitycontactinfo',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='address',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='telephone',
        ),
        migrations.AddField(
            model_name='businesscontactinfo',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='record.BusinessContact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entitycontactinfo',
            name='entity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='record.BusinessEntity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businesscontact',
            name='contact_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='businesscontact',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='businesscontact',
            name='position',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='businesscontactimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessentity',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='businessentity',
            name='entity_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categoryofcloth',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='cloth_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='grams_per_m2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='used_for',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='width',
            field=models.IntegerField(blank=True, default=150, null=True),
        ),
        migrations.AlterField(
            model_name='clothcategory',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshop',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshop',
            name='num_of_colors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshop',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshop',
            name='price_detail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshop',
            name='shop_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshopcolor',
            name='color_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clothinshopimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothmaterial',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothtexture',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfodata',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='entityimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entitypayment',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.PaymentAccount'),
        ),
        migrations.AlterField(
            model_name='entitypayment',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='entitypaymentimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entityrole',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.BusinessEntity'),
        ),
        migrations.AlterField(
            model_name='entityrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.PartnerType'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='stock_out_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='materialofcloth',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='partnertype',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentaccount',
            name='account_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.PaymentAccountData'),
        ),
        migrations.AlterField(
            model_name='paymentaccount',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.PaymentAccountType'),
        ),
        migrations.AlterField(
            model_name='paymentaccountdata',
            name='account_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paymentaccountdata',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentaccountdata',
            name='org_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paymentaccountdata',
            name='owner_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paymentaccounttype',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pieceofcloth',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pieceofcloth',
            name='manual_adjust',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rollofcloth',
            name='batch_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rollofcloth',
            name='color_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rollofcloth',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='textureofcloth',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='unitofcloth',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='UnitOfClothConversion',
        ),
        migrations.AddField(
            model_name='warehousecontactinfo',
            name='contact_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.ContactInfoData'),
        ),
        migrations.AddField(
            model_name='warehousecontactinfo',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Warehouse'),
        ),
    ]
