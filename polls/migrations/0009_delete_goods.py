# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_goods'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goods',
        ),
    ]
