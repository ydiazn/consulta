# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_mnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionEnfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CriterioClasificacionEnfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='clasificacionenfermedad',
            name='criterio',
            field=models.ForeignKey(to='nucleo.CriterioClasificacionEnfermedad'),
        ),
        migrations.AddField(
            model_name='clasificacionenfermedad',
            name='enfermedad',
            field=models.ForeignKey(to='nucleo.Enfermedad'),
        ),
    ]
