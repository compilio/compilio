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

        return JsonResponse({'ok': 'ok'})
