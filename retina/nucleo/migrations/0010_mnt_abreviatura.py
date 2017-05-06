# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0009_auto_20080101_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='mnt',
            name='abreviatura',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
