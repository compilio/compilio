import argparse
import contextlib
import io
import os
import sys
import uuid
import requests
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class File(models.Model):
    name = models.CharField(max_length=128)


class Folder(models.Model):
    name = models.CharField(max_length=128)
    compilio_path = models.CharField(max_length=128)
    user_path = models.CharField(max_length=128)
    sub_folders = models.ManyToManyField(File)


class Compiler(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=128)
    output_files_parse_code = models.TextField(null=True)

    remote_command = models.CharField(max_length=255)

    def get_input_files(self, command):
        input_files = []

        parser = argparse.ArgumentParser()
        parser.add_argument("input_files")
        arguments = command.split(' ')
        arguments.pop(0)
        args = parser.parse_args(arguments)

        input_files.append(args.input_files)

        return input_files

    def get_output_files(self, command):
        @contextlib.contextmanager
        def stdout_io(stdout=None):
            old = sys.stdout
            if stdout is None:
                stdout = io.StringIO()
            sys.stdout = stdout
            yield stdout
            sys.stdout = old

        set_command_code = "command = '" + command + "'\n"
        code = set_command_code + str(self.output_files_parse_code)

        with stdout_io() as s:
            exec(code)

        return s.getvalue()[:-1]


class Server(models.Model):
    ip = models.CharField(max_length=45)

    compilers = models.ManyToManyField(Compiler, through='ServerCompiler')


class ServerCompiler(models.Model):
    COMPILER_STATUS = (
        ('Alive', 'Alive'),
        ('Dead', 'Dead'),
    )

    port = models.IntegerField()
    compiler = models.ForeignKey(Compiler)
    server = models.ForeignKey(Server)
    last_used_date = models.DateTimeField(default=timezone.now)
    last_check = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=5, choices=COMPILER_STATUS)


def generate_id():
    while True:
        try:
            unique_id = uuid.uuid4().hex[:16]
            Task.objects.get(id=unique_id)
        except Task.DoesNotExist:
            return unique_id


class Task(models.Model):
    TASK_STATUS = (
        ('PENDING', 'PENDING'),
        ('COMPILING', 'COMPILING'),
        ('SUCCESS', 'SUCCESS'),
        ('ERROR', 'ERROR'),
    )

    id = models.CharField(primary_key=True, max_length=100, blank=True, unique=True, default=generate_id)

    command = models.CharField(max_length=128)
    submitted_date = models.DateTimeField(default=timezone.now)
    terminated_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=TASK_STATUS, default='PENDING')
    session_id = models.CharField(max_length=255, default='', null=True)
    owners = models.ManyToManyField(User, default=None)

    inputs = models.ManyToManyField(Folder, related_name='inputs')
    outputs = models.ManyToManyField(Folder, related_name='outputs')
    compiler = models.ForeignKey(Compiler, null=True, blank=True)
    server_compiler = models.ForeignKey(ServerCompiler, null=True, blank=True)

    input_file = models.CharField(max_length=255)

    output_logs = models.TextField(blank=True, null=True)

    @staticmethod
    def __save_output_file(task_id, res):
        filename = Task.get_output_files_path(task_id)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w+b') as f:
            f.write(res.content)

    def get_save_output_files(self):
        res = requests.get(self.server_compiler.server.ip + ':'
                           + str(self.server_compiler.port)
                           + '/get_output_files?id=' + self.id)
        if res.status_code == 200:
            Task.__save_output_file(self.id, res)

    def output_files_path(self):
        return Task.get_output_files_path(self.id)

    @staticmethod
    def get_output_files_path(task_id):
        return 'uploads/tasks/' + task_id + '/output.zip'

    def get_parsed_remote_command(self):
        return self.compiler.remote_command.replace('$input', self.input_file)
