from django.contrib import admin
from .models import Departamento #Importo la tabla

# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'anulate'
    )
    # list_display_links = ('id', 'name')
    list_filter = ('name','anulate',)
    # list_editable = ('shor_name',)
    # search_fields = ('name', 'shor_name')
    # list_per_page = 10

admin.site.register(Departamento, DepartamentoAdmin)

