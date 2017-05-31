# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0021_auto_20170429_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='foto',
        ),
    ]
