# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0011_auto_20170506_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areasalud',
            options={'verbose_name': '\xc1rea de salud', 'verbose_name_plural': '\xc1reas de salud'},
        ),
        migrations.AlterModelOptions(
            name='diagnostico',
            options={'verbose_name': 'Diagn\xf3stico'},
        ),
        migrations.AlterModelOptions(
            name='enfermedad',
            options={'verbose_name_plural': 'Enfermedades'},
        ),
        migrations.AlterModelOptions(
            name='especialidad',
            options={'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AlterModelOptions(
            name='medico',
            options={'verbose_name': 'M\xe9dico'},
        ),
        migrations.AlterModelOptions(
            name='unidadasistencial',
            options={'verbose_name': 'Unidad asistencial', 'verbose_name_plural': 'Unidades asistenciales'},
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
