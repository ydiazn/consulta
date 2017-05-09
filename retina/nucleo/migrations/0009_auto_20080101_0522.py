# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0008_conducta_abreviatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conducta',
            name='abreviatura',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
