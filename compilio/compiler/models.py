import datetime

from django.db import models


class File(models.Model):
    name = models.CharField(max_length=128)


class Folder(models.Model):
    name = models.CharField(max_length=128)
    compilio_path = models.CharField(max_length=128)
    user_path = models.CharField(max_length=128)
    sub_folders = models.ManyToManyField(File)


class Task(models.Model):
    token = models.CharField(max_length=128, primary_key=True)
    command = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    submitted_date = models.DateField(default=datetime.datetime.now)
    terminated_date = models.DateField(default=datetime.datetime.now)
    expiry_date = models.DateField(default=datetime.datetime.now)

    TASK_STATUS = (
        ('Pending', 'Pending'),
        ('Compiling', 'Compiling'),
        ('Terminated', 'Terminated'),
        ('Error', 'Error'),
    )
    status = models.CharField(max_length=10, choices=TASK_STATUS)

    inputs = models.ManyToManyField(Folder, related_name='inputs')
    outputs = models.ManyToManyField(Folder, related_name='outputs')


class Compiler(models.Model):
    name = models.CharField(max_length=128)
    regex = models.CharField(max_length=128)


class Server(models.Model):
    ip = models.CharField(max_length=45)

    compilers = models.ManyToManyField(Compiler, through='ServerCompiler')


class ServerCompiler(models.Model):
    port = models.IntegerField()
    compiler = models.ForeignKey(Compiler)
    server = models.ForeignKey(Server)

    last_used_date = models.DateField(default=datetime.datetime.now)
    last_check = models.DateField(default=datetime.datetime.now)

    COMPILER_STATUS = (
        ('Alive', 'Alive'),
        ('Dead', 'Dead'),
    )
    status = models.CharField(max_length=5, choices=COMPILER_STATUS)
