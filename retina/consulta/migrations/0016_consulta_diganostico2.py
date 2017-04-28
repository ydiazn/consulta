# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0006_diagnostico'),
        ('consulta', '0015_auto_20170428_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='diganostico2',
            field=models.ManyToManyField(to='nucleo.Diagnostico'),
        ),
    ]
