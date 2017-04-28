# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0004_auto_20080101_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=45)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=40)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('especialidad', models.ForeignKey(to='nucleo.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadAsistencial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=45)),
                ('direccion', models.TextField(blank=True)),
            ],
        ),
    ]
