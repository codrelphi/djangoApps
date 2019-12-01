from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task

def index(request):
    context = {
        "tasks": Task.objects.all()
    }
    return render(request, "taskslist/index.html", context)

def addTask(request):
    try:
        name = request.POST['task-name']
    except:
        return render(request, "taskslist/error.html", {"message": "No Task."})

    Task(name=name).save()
    return HttpResponseRedirect(reverse("index"))
