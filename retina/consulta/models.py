# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from dateutil.relativedelta import relativedelta
from django.db import models
from nucleo.models import (
    AreaSalud, MNT, ClasificacionEnfermedad, Medico, UnidadAsistencial, Diagnostico, Conducta, Especialidad
)
from datetime import date
from utils import historia_from_ci

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
    # foto = models.ImageField(upload_to='pacientes', blank=True)

    class Meta:
        verbose_name_plural = 'Pacientes'
        ordering = ('-id',)


    def save(self, *args, **kwargs):
        self.numero_historia_clinica = historia_from_ci(self.ci)
        super(Paciente, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %s %s" % (self.nombres, self.primer_apellido, self.segundo_apellido)

    @property
    def nombre_completo(self):
        return self.__unicode__()

    @property
    def edad(self):
        return relativedelta(date.today(), self.fecha_nacimiento).years


class Consulta(models.Model):
    especialidad = models.ForeignKey(Especialidad)
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)
    unidad = models.ForeignKey(UnidadAsistencial)
    fecha = models.DateTimeField()
    caso_nuevo = models.BooleanField(default=True)
    diagnostico = models.ManyToManyField(Diagnostico)
    conducta = models.ForeignKey(Conducta)
    mnt = models.ManyToManyField(MNT)

    class Meta:
        ordering = ('fecha',)

    def __unicode__(self):
        return "No. HC: %s( %s )-%s" % (self.paciente.numero_historia_clinica, self.paciente, self.fecha)
