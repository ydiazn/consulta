# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0008_auto_20080101_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cargo',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='centro_trabajo',
            field=models.CharField(max_length=45, blank=True),
        ),
    ]
