# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20160425_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_tex', models.CharField(max_length=200)),
                ('shipment_date', models.DateField(auto_now_add=True)),
                ('shipment_time', models.TimeField(auto_now_add=True)),
                ('shipment_sum', models.IntegerField()),
            ],
        ),
    ]
