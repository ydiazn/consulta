# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0007_conducta'),
        ('consulta', '0020_auto_20170429_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='caso_nuevo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='conducta',
            field=models.ForeignKey(default=1, to='nucleo.Conducta'),
            preserve_default=False,
        ),
    ]
