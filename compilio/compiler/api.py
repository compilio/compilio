from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def init(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        if command is None:
            return HttpResponse("command is None")

        return HttpResponse("OK")
