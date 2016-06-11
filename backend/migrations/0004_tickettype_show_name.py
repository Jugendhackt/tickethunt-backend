# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20160611_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='show_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tickettype_show', to='backend.TicketTypeAlias'),
            preserve_default=False,
        ),
    ]
