# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-14 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0002_betaaccessvm'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BetaAccessVM',
            new_name='BetaAccessVMType',
        ),
    ]
