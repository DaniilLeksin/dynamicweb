# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-23 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0004_auto_20160328_1434'),
        ('cms', '0014_auto_20160404_1908'),
        ('ungleich_page', '0011_ungleichproduct_ungleichproductitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='UngleichCustomer',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ungleich_page.Service')),
                ('section_class', models.CharField(blank=True, default='', max_length=100)),
                ('carousel_data_interval', models.IntegerField(default=3000)),
                ('bottom_text', djangocms_text_ckeditor.fields.HTMLField(default='<h3 class="section-subheading text-muted">*ungleich means not equal to (≠) U+2260.</h3>')),
            ],
            options={
                'abstract': False,
            },
            bases=('ungleich_page.service',),
        ),
        migrations.CreateModel(
            name='UngleichCustomerItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(blank=True, default='', max_length=300)),
                ('description', djangocms_text_ckeditor.fields.HTMLField()),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_item_image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
