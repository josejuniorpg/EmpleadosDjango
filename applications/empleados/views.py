from django.shortcuts import render
from django.views.generic import ListView
#Models
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 1 #Solo mostrara 4 regitros
    # ordering = 'first_name' #Ordena por nombre alfabeticamnete
    #context_object_name = 'empleados' #Lo comento porque uso el Objetc_list directamente
    # model = Empleado
    queryset = Empleado.objects.filter(
        departamento__name = 'Nombnre'
    )

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

class ListEmpleadosByKword(ListView):
    """Listar empleados por trabjajo"""
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'
    model = Empleado

    def get_queryset(self):
        #print('**********')
        palabra_clave = self.request.GET.get('kword', '') #Recibo parametro de Url, oh solicitudes que se mandar el servidor.
        #print('palabra_clave: ', palabra_clave)
        lista = Empleado.objects.filter( #Filtro lo que recibo en la Url.
            first_name = palabra_clave
        )
        #print('lista: ', lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        habilidades = Empleado.objects.get(id = 1)
        return habilidades.habilidades.all() #Retorno todas las habilidades del empleado con id = 1




