# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Especialidades'


class Medico(models.Model):
    nombres = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Especialidad)

    def __unicode__(self):
        return "%s %s %s" % (self.nombres, self.primer_apellido, self.segundo_apellido)

    class Meta:
        verbose_name = 'Médico'


class UnidadAsistencial(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    direccion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Unidad asistencial'
        verbose_name_plural = 'Unidades asistenciales'


class Diagnostico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Diagnóstico'


class Conducta(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    abreviatura = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(
        max_length=45,
        unique=True
    )

    def __unicode__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(
        max_length=45,
        unique=True
    )
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return self.nombre


class AreaSalud(models.Model):
    nombre = models.CharField(
        max_length=45,
        unique=True
    )
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Área de salud'
        verbose_name_plural = 'Áreas de salud'


# Medicina natural tradicional
class MNT(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    abreviatura = models.CharField(max_length=10, unique=True)
    
    def __unicode__(self):
        return self.abreviatura


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Enfermedades'


class CriterioClasificacionEnfermedad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre


class ClasificacionEnfermedad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    enfermedad = models.ForeignKey(Enfermedad)
    criterio = models.ForeignKey(CriterioClasificacionEnfermedad)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre
