# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0011_auto_20170506_1202'),
        ('consulta', '0022_remove_paciente_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='especialidad',
            field=models.ForeignKey(default=1, to='nucleo.Especialidad'),
            preserve_default=False,
        ),
    ]
