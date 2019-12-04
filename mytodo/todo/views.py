from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo

def index(request):
    context = {
        "todo_list": Todo.objects.all()
    }
    return render(request, "todo/index.html", context)

def add(request):
    todo = request.POST['todo-input']
    if len(todo) > 0:
        Todo(name=todo).save()

    return HttpResponseRedirect(reverse("index"))

def delete(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse("index"))
