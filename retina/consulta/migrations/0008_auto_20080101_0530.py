# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0007_paciente_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='cargo',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='centro_trabajo',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
