from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo

def index(request):
    context = {
        "todo_list": Todo.objects.all()
    }
    return render(request, "todo/index.html", context)

# TODO: pouvoir faire la redirection tout en affichant le contenu de la
# variable "message"
def add(request):
    todo = request.POST['todo-input']
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
    #return HttpResponseRedirect(reverse("index"), context)

def delete(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse("index"))
