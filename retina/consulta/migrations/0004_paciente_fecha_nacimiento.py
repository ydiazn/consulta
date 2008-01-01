# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_auto_20080101_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2017, 4, 21, 19, 23, 26, 148531, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
