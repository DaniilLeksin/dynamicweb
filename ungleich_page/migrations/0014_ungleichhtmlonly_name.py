# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-24 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ungleich_page', '0013_ungleichhtmlonly'),
    ]

    operations = [
        migrations.AddField(
            model_name='ungleichhtmlonly',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]