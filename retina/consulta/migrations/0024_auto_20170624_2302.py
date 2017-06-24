# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0023_consulta_especialidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Pacientes'},
        ),
    ]
