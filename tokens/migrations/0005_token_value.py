# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0004_auto_20160417_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='value',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
