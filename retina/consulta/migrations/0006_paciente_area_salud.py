# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_areasalud'),
        ('consulta', '0005_auto_20170421_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='area_salud',
            field=models.ForeignKey(default=1, to='nucleo.AreaSalud'),
            preserve_default=False,
        ),
    ]
