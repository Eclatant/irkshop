# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20161025_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custom_order',
            field=models.TextField(blank=True, null=True),
        ),
    ]
