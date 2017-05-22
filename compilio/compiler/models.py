import re
import uuid

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
    regex = models.CharField(max_length=128)
    docker_prefix_command = models.CharField(max_length=128, default='')

    def get_input_files(self, command):
        input_files = []
        matches = re.finditer(self.regex, command)
        for match_num, match in enumerate(matches):
            match_num = match_num + 1
            print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=match_num, start=match.start(),
                                                                                end=match.end(), match=match.group()))
            input_files.append(match.group())
            for group_num in range(0, len(match.groups())):
                group_num = group_num + 1

                print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=group_num,
                                                                                start=match.start(group_num),
                                                                                end=match.end(group_num),
                                                                                group=match.group(group_num)))
        return input_files


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


class Task(models.Model):
    TASK_STATUS = (
        ('Pending', 'Pending'),
        ('Compiling', 'Compiling'),
        ('Terminated', 'Terminated'),
        ('Error', 'Error'),
    )

    id = models.CharField(primary_key=True, max_length=100, blank=True, unique=True, default=uuid.uuid4)
    command = models.CharField(max_length=128)
    submitted_date = models.DateTimeField(default=timezone.now)
    terminated_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=TASK_STATUS, default='Pending')

    inputs = models.ManyToManyField(Folder, related_name='inputs')
    outputs = models.ManyToManyField(Folder, related_name='outputs')
    compiler = models.ForeignKey(Compiler, null=True, blank=True)
    server_compiler = models.ForeignKey(ServerCompiler, null=True, blank=True)
