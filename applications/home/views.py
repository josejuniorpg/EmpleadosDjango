from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home.html' #El archivo html que se va a renderizar y esta en templates
