# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-20 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ungleich_page', '0005_auto_20171019_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutitem',
            name='link_url',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]
