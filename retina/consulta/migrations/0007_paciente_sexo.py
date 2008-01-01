# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0006_paciente_area_salud'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(default='M', max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=False,
        ),
    ]
