import mimetypes
import os
import shutil

import requests
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests.exceptions import ConnectionError

from compilio.compiler.models import Compiler, ServerCompiler
from compilio.compiler.models import Task


def validate_post_arg(request, *keys):
    if request.method != 'POST':
        raise Exception('Use Method POST')

    arguments = []
    for key in keys:
        argument = request.POST.get(key)
        if argument is None:
            raise Exception(key + ' is None')
        arguments.append(argument)
        print(argument)

    if len(keys) == 1:
        return arguments[0]

    return arguments


def list_compilers(request):
    return JsonResponse({'compilers': serializers.serialize('json', Compiler.objects.all())})


@csrf_exempt
def init(request):
    try:
        command = validate_post_arg(request, 'command')
    except Exception as e:
        return HttpResponse(e, status=400)

    compiler_name = command.split(' ')[0]

    try:
        compiler_object = Compiler.objects.get(name=compiler_name)
    except Compiler.DoesNotExist:
        return HttpResponse('No compiler found', status=404)

    task = Task(command=command, compiler=compiler_object)

    if request.session is not None:
        task.session_id = request.session.session_key

    input_files = compiler_object.get_input_files(command)
    task.input_file = input_files[0]

    task.save()

    return JsonResponse({'input_files': input_files, 'task_id': task.id})


def save_files(request, task_id, folder):
    file = request.FILES['0']  # TODO : hardcoded key
    fs = FileSystemStorage()
    filename = fs.save('uploads/tasks/' + task_id + '/' + folder + '/' + file.name, file)
    uploaded_file_url = fs.url(filename)
    return uploaded_file_url


@csrf_exempt
def upload(request):
    try:
        task_id = validate_post_arg(request, 'task_id')
    except Exception as e:
        return HttpResponse(e, status=400)

    try:
        task_object = Task.objects.get(id=task_id)
    except Compiler.DoesNotExist:
        print('No Task found')
        return HttpResponse('No Task found', status=404)

    uploaded_file_url = save_files(request, task_id, 'input_files')

    # TODO : Find the correct runner (find currently the first in the db)
    server_compiler = ServerCompiler.objects.get(compiler=task_object.compiler)

    task_object.server_compiler = server_compiler
    task_object.save()

    output_files = server_compiler.compiler.get_output_files(task_object.command)

    try:
        print(task_object.get_parsed_remote_command())
        requests.post(server_compiler.server.ip + ':' + str(server_compiler.port) + '/compile',
                      data={'task_id': task_id,
                            'output_files': output_files,
                            'bash': task_object.get_parsed_remote_command()},
                      files={'0': open(uploaded_file_url, 'rb')})
    except ConnectionError:
        return send_failure(task_object)

    task_object.status = 'COMPILING'
    task_object.save()

    return JsonResponse({'ok': uploaded_file_url})


@csrf_exempt
def task(request):
    try:
        task_object = Task.objects.get(id=request.GET.get('task_id'))
    except Task.DoesNotExist:
        return JsonResponse({'error': 'task_id not found'}, status=404)

    if task_object.server_compiler is None:
        return send_failure(task_object)

    try:
        res = requests.get(task_object.server_compiler.server.ip + ':'
                           + str(task_object.server_compiler.port) + '/task?id=' + task_object.id)
    except ConnectionError:
        return send_failure(task_object)

    if res.status_code != 200:
        return send_failure(task_object)

    res_json = res.json()

    if os.path.isdir('uploads/tasks/' + task_object.id + '/output_files'):
        return JsonResponse(res_json)

    if res_json['state'] == 'SUCCESS':
        task_object.get_save_output_files()
        task_object.status = 'SUCCESS'
        task_object.save()

    return JsonResponse(res_json)


def send_failure(task_object):
    task_object.status = 'FAILED'
    task_object.save()

    return JsonResponse({'state': 'FAILED', 'output_log': '# Task was not executed'})


def serve_file(file_path, name):
    print(file_path)
    with open(file_path, 'rb') as f:
        data = f.read()

    response = HttpResponse(data, content_type=mimetypes.guess_type(file_path)[0])
    response['Content-Disposition'] = "attachment; filename={0}".format(name)
    response['Content-Length'] = os.path.getsize(file_path)

    return response


@csrf_exempt
def get_output_files(request):
    try:
        task_object = Task.objects.get(id=request.GET.get('task_id'))
    except Task.DoesNotExist:
        return JsonResponse({'error': 'task_id not found'}, status=404)

    path = Task.get_output_files_path(task_object.id)

    return serve_file(path, task_object.compiler.name + '_' + task_object.id + '.zip')


@csrf_exempt
def delete_task(request):
    try:
        task_object = Task.objects.get(id=request.GET.get('task_id'))
    except Task.DoesNotExist:
        return JsonResponse({'error': 'task_id not found'}, status=404)

    if (task_object.owners.count() > 0 and not task_object.owners.filter(id=request.user.id).exists()) or (
                    request.session.session_key is not None and task_object.session_id != request.session.session_key):
        return JsonResponse({'error': 'You dont own this task'}, status=404)

    shutil.rmtree('uploads/tasks/' + task_object.id + '/', ignore_errors=True)
    task_object.delete()

    return JsonResponse({'success': 'success'})
