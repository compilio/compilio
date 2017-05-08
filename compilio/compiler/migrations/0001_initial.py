# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('regex', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('compilio_path', models.CharField(max_length=128)),
                ('user_path', models.CharField(max_length=128)),
                ('sub_folders', models.ManyToManyField(to='compiler.File')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ServerCompiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField()),
                ('last_used_date', models.DateField()),
                ('last_check', models.DateField()),
                ('status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead')], max_length=5)),
                ('compiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compiler.Compiler')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compiler.Server')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('command', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('submitted_date', models.DateField()),
                ('terminated_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Compiling', 'Compiling'), ('Terminated', 'Terminated'), ('Error', 'Error')], max_length=10)),
                ('inputs', models.ManyToManyField(related_name='inputs', to='compiler.Folder')),
                ('outputs', models.ManyToManyField(related_name='outputs', to='compiler.Folder')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='compilers',
            field=models.ManyToManyField(through='compiler.ServerCompiler', to='compiler.Compiler'),
        ),
    ]