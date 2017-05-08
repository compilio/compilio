from django.conf import settings
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'compiler/index.html')


def tasks(request):
    return render(request, 'compiler/tasks.html')


def task(request, task):
    # Todo: add voter to check if the task can be read by current (or anonymous) user

    return render(request, 'compiler/task.html')
