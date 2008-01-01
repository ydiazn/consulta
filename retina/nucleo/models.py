from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre = CharField(
        max_length=45, 
        unique=True,
        verbose_name_plural='Provincias'
    )


class Municipio(models.Model):
    nombre = CharField(
        max_length=45, 
        unique=True,
        verbose_name_plural='Municipios'
    )
    provincia = models.ForeignKey(Provincia)