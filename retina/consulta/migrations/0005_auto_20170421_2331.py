# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_paciente_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='municipio',
        ),
        migrations.AddField(
            model_name='paciente',
            name='numero_historia_clinica',
            field=models.CharField(default='1', max_length=11),
            preserve_default=False,
        ),
    ]
