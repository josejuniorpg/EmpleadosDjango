from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('new-departamento', views.NewDepartamentoView.as_view(), name='new-departamento'),
]