from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.home.models import Prueba
from applications.departamento.models import Departamento


# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html' #El archivo html que se va a renderizar y esta en templates

class PruebaListView(ListView):
    template_name = 'home/vista.html'
    queryset = ['1','2','3','4','5','6','7','8','9','10'] #Lista de numeros que se van a mostrar en la lista
    context_object_name = 'listaNumeros' #Nombre de la lista que se va a mostrar en el html

class ModeloPruebaListView(ListView):
    template_name = 'home/pruebas.html'
    model = Prueba
    context_object_name = 'listaPrueba' #Nombre de la lista que se va a mostrar en el html