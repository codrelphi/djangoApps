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

    if len(name) > 0:
        Task(name=name).save()
    return HttpResponseRedirect(reverse("index"))

def delete_task(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return HttpResponseRedirect(reverse("index"))
