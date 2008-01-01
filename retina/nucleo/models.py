from django.db import models

# Create your models here.

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


#Medicina natural tradicional
class MNT(models.Model):
    nombre = models.CharField(
        max_length=100, 
        unique=True
    )
    
    def __unicode__(self):
        return self.nombre


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