from django.shortcuts import render
from django.views.generic import ListView
#Models
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    # paginate_by = 4
    # ordering = 'first_name'
    #context_object_name = 'empleados' #Lo comento porque uso el Objetc_list directamente
    model = Empleado

class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'empleados/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['name'] #Recibo parametro de Url.
        #Contenido de la lista
        lista = Empleado.objects.filter(
            departamento__name = area #Busco el atributo name del modelo departamento
        )
        return lista #el meotodo siempre debe retornar una lista.

