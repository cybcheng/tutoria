# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutorial', '0001_initial'),
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutors.Tutor'),
        ),
    ]
