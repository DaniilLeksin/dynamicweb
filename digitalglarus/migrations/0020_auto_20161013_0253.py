# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalglarus', '0019_auto_20160929_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingorder',
            name='cc_brand',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='bookingorder',
            name='last4',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='membershiporder',
            name='cc_brand',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='membershiporder',
            name='last4',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
