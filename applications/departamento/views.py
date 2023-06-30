from django.shortcuts import render
from django.views.generic.edit import (FormView)
from django.views.generic import (TemplateView, ListView, UpdateView, DeleteView)
from .forms import (NewDepartamento)
from django.urls import reverse_lazy

from .models import Departamento
from ..empleados.models import Empleado


# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new-departamento.html'
    form_class = NewDepartamento
    success_url = reverse_lazy('empleado_app:success')
    def form_valid(self, form):
        print('**********Estamos en el form_valid**********')
        print(form.cleaned_data)
        name, short_name, first_name, last_name = form.cleaned_data.values()
        Empleado.objects.create(#ORM Django
            first_name = first_name,
            last_name = last_name,
            job = '1',
            departamento = Departamento.objects.create(
                name = name,
                short_name = short_name
            )
        )
        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento


class DepartamentoUpdateView(UpdateView):
    template_name = 'departamento/detail.html'
    model = Departamento
    fields = [ #Este campo es obligatorio.
        'name', #Son campos de mi modelo.
        'short_name',
        'anulate',
    ]
    success_url = reverse_lazy('empleado_app:success')
    context_object_name = 'departamento' #Es el nombre que se le da al objeto en el template.

class DepartamentoDeleteView(DeleteView):
    template_name = 'departamento/delete.html'
    model = Departamento
    context_object_name = 'departamento'
    success_url = reverse_lazy('empleado_app:success')


