# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0004_auto_20080101_0613'),
        ('consulta', '0012_remove_consulta_diagnostico'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='diagnostico',
            field=models.ManyToManyField(to='nucleo.ClasificacionEnfermedad'),
        ),
    ]
