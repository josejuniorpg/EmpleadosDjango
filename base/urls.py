from django.contrib import admin
from django.urls import path, include
from applications.home.views import IndexView
from applications.empleados.views import ListAllEmpleados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('', include('applications.empleados.urls')),
]
