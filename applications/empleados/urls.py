from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('test/', views.ListAllEmpleados.as_view()),
]