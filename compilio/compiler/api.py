import re

from django.http import HttpResponse
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

        matches = re.finditer(compiler_object.regex, command)
        for match_num, match in enumerate(matches):
            match_num = match_num + 1
            print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=match_num, start=match.start(),
                                                                                end=match.end(), match=match.group()))
            for group_num in range(0, len(match.groups())):
                group_num = group_num + 1

                print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=group_num,
                                                                                start=match.start(group_num),
                                                                                end=match.end(group_num),
                                                                                group=match.group(group_num)))

        return HttpResponse('output_files')
