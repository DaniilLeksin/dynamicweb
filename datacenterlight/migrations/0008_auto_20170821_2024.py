# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-21 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0007_stripeplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripeplan',
            name='stripe_plan_id',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
