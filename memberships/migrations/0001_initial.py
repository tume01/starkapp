# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initialDate', models.DateField()),
                ('finalDate', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('guests', models.IntegerField()),
                ('price', models.FloatField()),
                ('billing', models.TextField(max_length=200)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberships.MembershipType'),
        ),
    ]
