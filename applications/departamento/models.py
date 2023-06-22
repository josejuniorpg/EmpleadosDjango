from django.db import models

# Create your models here.

class Departamento (models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self): #Es recomendable poner los Str.
        return str(self.id) + '-' + self.name + '-' + self.short_name
