# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0006_diagnostico'),
        ('consulta', '0018_auto_20170428_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='mnt',
        ),
        migrations.AddField(
            model_name='consulta',
            name='mnt',
            field=models.ManyToManyField(to='nucleo.MNT'),
        ),
    ]
