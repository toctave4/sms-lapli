# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pri_mache', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Observation_prix',
            new_name='ObservationDePrix',
        ),
        migrations.RenameModel(
            old_name='Type_Marche',
            new_name='TypeMarche',
        ),
        migrations.RenameModel(
            old_name='Type_Produit',
            new_name='TypeProduit',
        ),
    ]
