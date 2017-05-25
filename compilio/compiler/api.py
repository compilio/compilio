import os

import requests
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

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
        print('No compiler found')
        return HttpResponse('No compiler found', status=404)

    task = Task(command=command, compiler=compiler_object)
    task.save()

    # TODO : Task status to 'pending'

    input_files = compiler_object.get_input_files(command)

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

    res = requests.post(server_compiler.server.ip + ':' + str(server_compiler.port) + '/compile',
                        data={'task_id': task_id,
                              'output_files': output_files,
                              'bash': task_object.server_compiler.compiler.docker_prefix_command + ' ' + task_object.command},
                        files={'0': open(uploaded_file_url, 'rb')})
    # TODO : param task_id, input_files

    # TODO : Create files rows in bd and attach it to Task object
    # TODO : Get build process (here or in 'init' endpoint)
    # TODO : Send process_build and input files to compiler-runner
    # TODO : Task status to 'Sent to runner'

    return JsonResponse({'ok': uploaded_file_url})


@csrf_exempt
def task(request):
    try:
        task_object = Task.objects.get(id=request.GET.get('id'))
    except Task.DoesNotExist:
        return JsonResponse({'error': 'task_id not found'})

    res = requests.get(task_object.server_compiler.server.ip + ':'
                       + str(task_object.server_compiler.port) + '/task?id=' + task_object.id)

    res_json = res.json()

    if os.path.isdir('uploads/tasks/' + task_object.id + '/output_files'):
        return JsonResponse(res_json)

    if res_json['state'] == 'SUCCESS':
        task_object.get_save_output_files()

    return JsonResponse(res_json)


def serve_file(file_path):
    response = HttpResponse(
        content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(os.path.basename(file_path))
    response['X-Sendfile'] = smart_str(file_path)
    return response


@csrf_exempt
def get_output_files(request):
    try:
        task_object = Task.objects.get(id=request.GET.get('id'))
    except Task.DoesNotExist:
        return JsonResponse({'error': 'task_id not found'})

    path = Task.get_output_files_path(task_object.id)

    return serve_file(path)
