# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20160409_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
    ]
