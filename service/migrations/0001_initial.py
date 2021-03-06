# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 19:07
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address_main_office', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('point_name', models.CharField(max_length=100)),
                ('price_for_one', models.CharField(max_length=100)),
                ('provider_type', models.CharField(max_length=100)),
                ('provider', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='location',
                    to='service.Provider'
                )),
            ],
        ),
    ]
