# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0019_auto_20170429_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='diganostico',
            new_name='diagnostico',
        ),
    ]
