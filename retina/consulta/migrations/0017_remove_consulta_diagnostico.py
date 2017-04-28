# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0016_consulta_diganostico2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='diagnostico',
        ),
    ]
