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