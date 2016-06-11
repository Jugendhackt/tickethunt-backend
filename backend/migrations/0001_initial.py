# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 12:16
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('persons', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='./tickets/')),
                ('valid_until', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TicketTypeAlias',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='tickettype',
            name='alias',
            field=models.ManyToManyField(to='backend.TicketTypeAlias'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.ManyToManyField(to='backend.TicketType'),
        ),
    ]
