# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20160408_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioneditem',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auctioneditem',
            name='will_sell',
            field=models.BooleanField(default=True),
        ),
    ]
