from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from compilio.compiler.models import Task


@csrf_exempt
def init(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        if command is None:
            return HttpResponse("command is None")

        task = Task(token='t4VQ7J51K67a0rFQ4jq1pZd7WgMgN95S', command=command)
        task.save()

        return HttpResponse('output_files')
