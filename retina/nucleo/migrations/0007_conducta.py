# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0006_diagnostico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conducta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=45)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
    ]
