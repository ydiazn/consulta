# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0010_mnt_abreviatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mnt',
            name='abreviatura',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
