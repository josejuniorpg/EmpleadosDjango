from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#Models
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4 #Numero de registros por pagina
    # ordering = 'first_name' #Ordena por nombre alfabeticamnete
    #context_object_name = 'empleados' #Lo comento porque uso el Objetc_list directamente
    #model = Empleado
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '') #Recibo parametro de Url, oh solicitudes que se mandar el servidor.
        lista = Empleado.objects.filter( #Filtro lo que recibo en la Url.
            full_name__icontains = palabra_clave
        )
        return lista

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

    #Detail View

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/detail_empleado.html'
    context_object_name = 'empleados'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/add.html'
    fields = [ #Este campo es obligatorio.
        'first_name', #Son campos de mi modelo.
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    #success_url = '.' #Redirecciona a la misma pagina
    #success_url = '/' #Redirecciona al home
    #success_url = '/success/' #Redirecciona a la pagina de exito
    success_url = reverse_lazy('empleado_app:success')
    def form_valid(self, form): #Valida el formulario, y guardo en la BD.
        #Logica del proceso
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name #Concateno el nombre y apellido, y lo manndo al atribtuo
        print('Este es el empleado',empleado)
        empleado.save() #Guardo en la BD.
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'empleados/success.html'


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleados/update.html'
    model = Empleado
    fields = [ #Este campo es obligatorio.
        'first_name', #Son campos de mi modelo.
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('empleado_app:success')
    def post(self, request, *args, **kwargs):
        #Metodo para ver que se envia en el formulario
        self.object = self.get_object()# Obtengo el objeto que se va a actualizar, Pero lo puedo quitar
        print('********** METODO POST **********')
        print('POST: ', request.POST)
        print('POST: ', request.POST['last_name']) #Accedo a un campo en el request.
        print('FILES: ', request.FILES)
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    template_name = 'empleados/delete.html'
    model = Empleado
    success_url = reverse_lazy('empleado_app:success')
    context_object_name = 'empleados'

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


