# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0024_auto_20170624_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ('fecha',)},
        ),
    ]
