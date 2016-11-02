# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 12:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=10)),
                ('position', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessContactImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('path', models.FilePathField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessContact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessContactMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessContact')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryOfCloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_code', models.CharField(max_length=20)),
                ('cloth_name', models.CharField(blank=True, max_length=20)),
                ('width', models.IntegerField(blank=True, default=150)),
                ('used_for', models.CharField(blank=True, max_length=100)),
                ('grams_per_m2', models.FloatField(blank=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClothCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.CategoryOfCloth')),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='ClothColorMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClothImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('path', models.FilePathField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Cloth')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClothInShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_code', models.CharField(blank=True, max_length=10)),
                ('num_of_colors', models.IntegerField(blank=True, default=0)),
                ('price', models.FloatField(blank=True, default=0)),
                ('price_detail', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('added_time', models.DateField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Cloth')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessEntity')),
            ],
        ),
        migrations.CreateModel(
            name='ClothInShopColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_id', models.CharField(max_length=20)),
                ('color_name', models.CharField(blank=True, max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                (
                'cloth_in_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ClothInShop')),
            ],
        ),
        migrations.CreateModel(
            name='ClothInShopImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('path', models.FilePathField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                (
                'cloth_in_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ClothInShop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClothMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='ClothTexture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Cloth')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(
                    choices=[('tel', 'Telephone'), ('fax', 'Fax'), ('email', 'Email'), ('wechat', 'Wechat'),
                             ('address', 'Address'), ('website', 'Website'), ('other', 'Other')], default='tel',
                    max_length=10)),
                ('category', models.CharField(
                    choices=[('personal', 'Personal'), ('office', 'Office'), ('home', 'Home'), ('other', 'Other')],
                    default='personal', max_length=10)),
                ('content', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityContactMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('contact_method',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ContactInfoData')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessEntity')),
            ],
        ),
        migrations.CreateModel(
            name='EntityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('path', models.FilePathField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessEntity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityPaymentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('path', models.FilePathField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('entity_payment',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.EntityPayment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.BusinessEntity')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialOfCloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAccountData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=20)),
                ('org_name', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextureOfCloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texture_name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfCloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfClothConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.FloatField()),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('unit_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_from',
                                                to='base.UnitOfCloth')),
                ('unit_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_to',
                                              to='base.UnitOfCloth')),
            ],
        ),
        migrations.AddField(
            model_name='paymentaccount',
            name='account_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PaymentAccountData'),
        ),
        migrations.AddField(
            model_name='paymentaccount',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PaymentAccountType'),
        ),
        migrations.AddField(
            model_name='entityrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PartnerType'),
        ),
        migrations.AddField(
            model_name='entitypayment',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PaymentAccount'),
        ),
        migrations.AddField(
            model_name='entitypayment',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessEntity'),
        ),
        migrations.AddField(
            model_name='clothtexture',
            name='texture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.TextureOfCloth'),
        ),
        migrations.AddField(
            model_name='clothmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.MaterialOfCloth'),
        ),
        migrations.AddField(
            model_name='clothcolormap',
            name='cloth_external',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external',
                                    to='base.ClothInShopColor'),
        ),
        migrations.AddField(
            model_name='clothcolormap',
            name='cloth_internal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internal',
                                    to='base.ClothInShopColor'),
        ),
        migrations.AddField(
            model_name='businesscontactmethod',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ContactInfoData'),
        ),
        migrations.AddField(
            model_name='businesscontact',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BusinessEntity'),
        ),
    ]
