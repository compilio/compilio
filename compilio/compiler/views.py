from django.shortcuts import render

from .models import Task


def index(request):
    return render(request, 'compiler/index.html')


def tasks(request):
    return render(request, 'compiler/tasks.html')


def task(request, id):
    # Todo: add voter to check if the task can be read by current (or anonymous) user
    task = Task.objects.get(id=id)

    print(task)

    return render(request, 'compiler/task.html', {'task': task})


def documentation(request):
    return render(request, 'compiler/documentation.html')
