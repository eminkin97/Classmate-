# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='datetimeadded',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
