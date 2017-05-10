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
            return HttpResponse("command is None")

        compiler_name = command.split(' ')[0]

        try:
            compiler_object = Compiler.objects.get(name=compiler_name)
        except Compiler.DoesNotExist:
            print('No compiler found')
            return HttpResponse('No compiler found')

        task = Task(command=command)
        task.save()

        input_files = compiler_object.get_input_files(command)

        return JsonResponse({'input_files': input_files})
