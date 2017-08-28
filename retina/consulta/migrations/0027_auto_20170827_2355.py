# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0026_auto_20170825_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
