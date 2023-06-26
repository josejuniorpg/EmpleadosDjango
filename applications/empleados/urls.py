from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('listar_todo/', views.ListAllEmpleados.as_view()),
    path('listar_area/<name>/', views.ListByAreaEmpleado.as_view()),
    path('listar_area/<name>/', views.ListByAreaEmpleado.as_view()),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view()),
]