from django.shortcuts import render

from tasks.models import MyTasks


def homepage(request):
    context = {
        'tasks': MyTasks.objects.all(),
    }
    return render(request, 'index.html', context=context)
