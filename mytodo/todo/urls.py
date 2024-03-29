from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("edit/<int:todo_id>", views.edit, name="edit"),
    path("addedit/<int:todo_id>", views.add_edit, name="add_edit"),
    path("delete/<int:todo_id>", views.delete, name="delete")
]
