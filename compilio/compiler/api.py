from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from compilio.compiler.models import Compiler
from compilio.compiler.models import Task


@csrf_exempt
def init(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        if command is None:
            return HttpResponse("command is None", status=400)

        compiler_name = command.split(' ')[0]

        try:
            compiler_object = Compiler.objects.get(name=compiler_name)
        except Compiler.DoesNotExist:
            print('No compiler found')
            return HttpResponse('No compiler found', status=404)

        task = Task(command=command)
        task.save()

        # TODO : Task status to 'Waiting for input_files'

        input_files = compiler_object.get_input_files(command)

        return JsonResponse({'input_files': input_files, 'task_id': task.id})


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        if task_id is None:
            return HttpResponse("task_id is None", status=400)

        try:
            task_object = Task.objects.get(id=task_id)
        except Compiler.DoesNotExist:
            print('No Task found')
            return HttpResponse('No compiler found', status=404)

        print(task_object)
        # TODO : param task_id, input_files

        # TODO : Create files rows in bd and attach it to Task object
        # TODO : Store input files in /task_id/input_files
        # TODO : Get build process (here or in 'init' endpoint)
        # TODO : Send process_build and input files to compiler-runner
        # TODO : Task status to 'Sent to runner'

        return JsonResponse({'ok': 'ok'})


@csrf_exempt
def status(request):
    # TODO : param task_id
    # TODO : Get status from db
    # TODO : OR
    # TODO : Query compiler-runner to get status
    # TODO : Update status
    return JsonResponse({'ok': 'ok'})


@csrf_exempt
def receive_output_files(request):
    # TODO : Called by compiler_runner
    # TODO : param task_id, output_files

    # TODO : Store output_files in /task_id/input_files
    # TODO : Change status

    return JsonResponse({'ok': 'ok'})
