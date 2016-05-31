# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0001_initial'),
        ('users', '0001_initial'),
        ('events', '0005_auto_20160527_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='environment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='environment.Environment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
            preserve_default=False,
        ),
    ]
