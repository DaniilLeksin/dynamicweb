# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-09 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0018_auto_20180403_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCLCalculatorPluginModel',
            fields=[
                ('dclsectionpluginmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datacenterlight.DCLSectionPluginModel')),
            ],
            options={
                'abstract': False,
            },
            bases=('datacenterlight.dclsectionpluginmodel',),
        ),
        migrations.CreateModel(
            name='VMPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('vat_inclusive', models.BooleanField(default=True)),
                ('vat_percentage', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('cores_unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('ram_unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('ssd_unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('hdd_unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.AddField(
            model_name='dclcalculatorpluginmodel',
            name='pricing',
            field=models.ForeignKey(default=None, help_text='Choose a pricing that will be associated with this Calculator', on_delete=django.db.models.deletion.CASCADE, to='datacenterlight.VMPricing'),
        ),
    ]
