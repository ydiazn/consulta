# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0011_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='diagnostico',
        ),
    ]
