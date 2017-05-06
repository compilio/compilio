from django.conf import settings
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'compiler/index.html')


def tasks(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, 'compiler/tasks.html')
