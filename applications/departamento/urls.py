from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento', views.NewDepartamentoView.as_view(), name='new-departamento'),
    path('ver_departamento', views.DepartamentoListView.as_view(), name='departamento_list'),
    path('departamento_details/<pk>', views.DepartamentoUpdateView.as_view(), name='update'),
    path('departamento_eliminar/<pk>', views.DepartamentoDeleteView.as_view(), name='delete'),
]