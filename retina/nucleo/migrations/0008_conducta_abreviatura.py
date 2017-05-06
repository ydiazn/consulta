# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0007_conducta'),
    ]

    operations = [
        migrations.AddField(
            model_name='conducta',
            name='abreviatura',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
