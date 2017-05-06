from django.db import models


# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre


class Medico(models.Model):
    nombres = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Especialidad)

    def __unicode__(self):
        return "%s %s %s" % (self.nombres, self.primer_apellido, self.segundo_apellido)


class UnidadAsistencial(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    direccion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre


class Diagnostico(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre


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
