from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo
import logging as lg

def index(request):
    context = {
        "todo_list": Todo.objects.all()
    }
    return render(request, "todo/index.html", context)

def add(request):
    todo = request.POST['todo-input']
    todo = todo.strip()
    if len(todo) > 0:
        try:
            if Todo.objects.get(name=todo):
                message = "This task has already existed"
        except Todo.DoesNotExist:
            message=""
            Todo(name=todo).save()
    else:
        message = "Please, add a task!"

    context = {
        "todo_list": Todo.objects.all(),
        "message": message
    }
    return render(request, "todo/index.html", context)

def edit(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {
        "todo": todo
    }
    return render(request, "todo/edit.html", context)

def add_edit(request, todo_id):
    todo_name = request.POST['todo-edit-input']
    todo_name = todo_name.strip()
    if len(todo_name) > 0:
        try:
            if Todo.objects.get(name=todo_name):
                message = "This task has already existed!"
        except Todo.DoesNotExist:
            message=""
            task = Todo.objects.get(pk=todo_id)
            task.name = todo_name
            task.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        message = "Please, edit the task!"

    context = {
        "todo": Todo.objects.get(pk=todo_id),
        "message": message
    }
    return render(request, "todo/edit.html", context)

def delete(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse("index"))
