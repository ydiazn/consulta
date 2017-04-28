# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0014_auto_20170428_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
