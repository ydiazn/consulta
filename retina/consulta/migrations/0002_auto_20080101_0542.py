# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=40)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('ci', models.CharField(max_length=11)),
                ('direccion', models.TextField()),
                ('foto', models.ImageField(upload_to=b'pacientes')),
                ('municipio', models.ForeignKey(to='nucleo.Municipio')),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='municipio',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
