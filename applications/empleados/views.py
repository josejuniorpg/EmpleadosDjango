from django.shortcuts import render
from django.views.generic import ListView
#Models
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    # paginate_by = 4
    # ordering = 'first_name'
    # context_object_name = 'empleados'
    model = Empleado

