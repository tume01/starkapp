# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bungalows', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipoBungalow',
            new_name='BungalowType',
        ),
        migrations.RenameField(
            model_name='bungalow',
            old_name='tipoBungalow',
            new_name='bungalow_type_id',
        ),
        migrations.RenameField(
            model_name='bungalow',
            old_name='ubicacion',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='bungalow',
            old_name='estado',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='bungalow',
            old_name='numero',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='bungalowtype',
            old_name='aforo',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='bungalowtype',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='bungalowtype',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bungalowtype',
            old_name='precio',
            new_name='price',
        ),
    ]
