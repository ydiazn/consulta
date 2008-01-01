# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_mnt'),
        ('consulta', '0010_auto_20080101_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('diagnostico', models.TextField()),
                ('mnt', models.ForeignKey(to='nucleo.MNT')),
                ('paciente', models.ForeignKey(to='consulta.Paciente')),
            ],
        ),
    ]
