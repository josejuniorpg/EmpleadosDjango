from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar_todo/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar_area/<name>/', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar_habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver_empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('crear_empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='update'),
    path('delete_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete'),
]