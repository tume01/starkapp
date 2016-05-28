# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_type', '0002_auto_20160524_1701'),
        ('events', '0003_remove_event_event_type_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventType',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events_type.EventsType'),
        ),
    ]
