# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitedemesure',
            name='formule',
            field=models.TextField(verbose_name=b'Formule', blank=b'True'),
        ),
    ]
