from django.shortcuts import render, redirect
from django.http import Http404
import shutil

from .models import Task


def index(request):
    return render(request, 'compiler/index.html')


def tasks(request):
    tasks = []

    if request.user.is_authenticated():
        tasks = Task.objects.filter(owners__id=request.user.id)
    elif request.session.session_key is not None:
        tasks = Task.objects.filter(session_id=request.session.session_key)

    return render(request, 'compiler/tasks.html', {'tasks': tasks})


def task(request, id):
    task = Task.objects.get(id=id)

    if task.owners.count() > 0:
        if not task.owners.filter(id=request.user.id).exists():
            raise Http404()
    else:
        if request.user.is_authenticated():
            task.owners.add(request.user)
            task.save()

    if request.session.session_key is not None:
        task.session_id = request.session.session_key
        task.save()

    return render(request, 'compiler/task.html', {'task': task})


def documentation(request):
    return render(request, 'compiler/documentation.html')


def terms(request):
    return render(request, 'compiler/terms.html')


def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404()

    if (task.owners.count() > 0 and not task.owners.filter(id=request.user.id).exists()) or (
                    request.session.session_key is not None and task.session_id != request.session.session_key):
        raise Http404()  # User is not allowed but returning a 404 avoids him to know it.

    shutil.rmtree('uploads/tasks/' + task.id + '/', ignore_errors=True)
    task.delete()

    return redirect('tasks')
