# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0005_especialidad_medico_unidadasistencial'),
        ('consulta', '0013_consulta_diagnostico'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(default=1, to='nucleo.Medico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consulta',
            name='unidad',
            field=models.ForeignKey(default=1, to='nucleo.UnidadAsistencial'),
            preserve_default=False,
        ),
    ]
