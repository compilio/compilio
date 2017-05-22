# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:44
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0002_auto_20170506_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servercompiler',
            name='last_check',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AlterField(
            model_name='servercompiler',
            name='last_used_date',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='expiry_date',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='terminated_date',
            field=models.DateTimeField(default=timezone.now),
        ),
    ]
