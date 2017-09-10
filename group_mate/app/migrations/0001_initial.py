# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('section_numb', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('numLikes', models.IntegerField()),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_address_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Schools'),
        ),
    ]
