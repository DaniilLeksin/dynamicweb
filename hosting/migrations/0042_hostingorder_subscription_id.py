# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-17 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0041_userhostingkey_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostingorder',
            name='subscription_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
