# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0006_auto_20171113_2208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NotAvailableSlots',
            new_name='NotAvailableSlot',
        ),
    ]
