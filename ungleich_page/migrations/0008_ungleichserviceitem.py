# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-17 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0004_auto_20160328_1434'),
        ('ungleich_page', '0007_auto_20171117_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='UngleichServiceItem',
            fields=[
                ('serviceitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ungleich_page.ServiceItem')),
                ('data_replaced_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_item_data_replaced_image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('ungleich_page.serviceitem',),
        ),
    ]
