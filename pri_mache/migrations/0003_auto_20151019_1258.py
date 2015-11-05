# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri_mache', '0002_auto_20151009_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='observationdeprix',
            options={'verbose_name_plural': 'Observations de prix'},
        ),
    ]
