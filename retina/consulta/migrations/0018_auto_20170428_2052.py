# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0017_remove_consulta_diagnostico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='diganostico2',
            new_name='diganostico',
        ),
    ]
