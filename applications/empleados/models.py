from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    """Modelo para tabla habilidades"""
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """Modelo para tabla empleados"""
    JOB_CHOICES = ( #Array de selección de opciones para el campo job
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro'),
    )
    first_name = models.CharField('Nombres',max_length=50)
    last_name = models.CharField('Apellido',max_length=50)
    full_name = models.CharField('Nombre Completo',max_length=120, blank=True) #Con blank no sera obligatorio
    job= models.CharField('Trabajo',max_length=50, choices=[('0','Contador'), ('1','Administrador'),])
    #avatar = models.ImageField(upload_to='empleados', blank=True, null=True)

    #Relaciones
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)

    hoja_vida = RichTextField()
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Mis Empleados'
        ordering = ['first_name']
        unique_together = ('first_name','departamento') #No se puede repetir un empleado con el mismo nombre y departamento.

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name