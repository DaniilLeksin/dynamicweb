# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-03 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0017_auto_20180329_0056'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dclcontactpluginmodel',
            name='organization_name',
            field=models.CharField(blank=True, default='ungleich glarus ag', max_length=100),
        ),
        migrations.AlterField(
            model_name='dclfooterpluginmodel',
            name='copyright_label',
            field=models.CharField(blank=True, default='ungleich glarus ag', help_text='Name of the company alongside the copyright year', max_length=100),
        ),
        migrations.AddField(
            model_name='cmsintegration',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='cmsintegration',
            name='name',
            field=models.CharField(default='default', help_text='A unique name for the Integration. This name will be used to fetch the Integration into pages', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='cmsintegration',
            unique_together=set([('name', 'domain')]),
        ),
    ]