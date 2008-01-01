# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.db import models
from nucleo.models import AreaSalud, MNT
from datetime import date

# Create your models here.

class Paciente(models.Model):
    sexo_choices = (('M', 'Masculino'), ('F', 'Femenino'),)
    nombres = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    numero_historia_clinica = models.CharField(max_length=11)
    ci = models.CharField(max_length=11)
    sexo = models.CharField(choices=sexo_choices, max_length=1)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    area_salud = models.ForeignKey(AreaSalud)
    ocupacion = models.CharField(max_length=45, blank=True)
    centro_trabajo = models.CharField(max_length=45, blank=True)
    foto = models.ImageField(upload_to='pacientes', blank=True)
    
    def __unicode__(self):
        return "%s %s %s" % (self.nombres, self.primer_apellido, self.segundo_apellido)
    
    def edad(self):
        return 3


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    diagnostico = models.TextField()
    mnt = models.ForeignKey(MNT)

    def __unicode__(self):
        return "%No. HC: %s( %s )-%s" % (self.paciente.numero_historia_clinica, self.paciente, self.fecha)