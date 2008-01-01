from django.db import models
from nucleo.models import Municipio
from datetime import date

# Create your models here.

class Paciente(models.Model):
    nombres = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    ci = models.CharField(max_length=11)
    direccion = models.TextField()
    municipio = models.ForeignKey(Municipio)
    foto = models.ImageField(upload_to='pacientes')
    
    def __unicode__(self):
        return self.nombres
    
    def edad(self):
        return 3