from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('message', views.message),
    path('hello/msg', views.message)
]
