# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('hydromet', '0001_initial'),
        ('pri_mache', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_collecte', models.DateTimeField(auto_now_add=True)),
                ('prix', models.DecimalField(default=0, verbose_name=b'Prix', max_digits=8, decimal_places=2)),
                ('collecteur', models.ForeignKey(related_name='collecteur', verbose_name=b'Collecteur', to='base.PersonneContact')),
            ],
        ),
        migrations.RemoveField(
            model_name='marche',
            name='siteSentinelle',
        ),
        migrations.AddField(
            model_name='marche',
            name='sectionCommunale',
            field=models.ForeignKey(verbose_name=b'Section Communale', to='base.SectionCommunale', null=True),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='description',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='observateur',
            field=models.ForeignKey(to='base.PersonneContact', null=True),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='valider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='observationdeprix',
            name='date_collecte',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date collecte de donnees'),
        ),
        migrations.AddField(
            model_name='log',
            name='marche',
            field=models.ForeignKey(verbose_name=b'Marche', to='pri_mache.Marche'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(default=None, blank=True, to='pri_mache.ObservationDePrix', null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='produit',
            field=models.ForeignKey(verbose_name=b'Produit', to='pri_mache.Produit'),
        ),
        migrations.AddField(
            model_name='log',
            name='unitemesure',
            field=models.ForeignKey(verbose_name=b'Unite de mesure', to='hydromet.UniteDeMesure'),
        ),
    ]
