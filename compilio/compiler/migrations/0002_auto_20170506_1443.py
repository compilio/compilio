# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='submitted_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]