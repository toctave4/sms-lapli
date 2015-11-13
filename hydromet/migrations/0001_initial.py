# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(null=True, verbose_name=b'Temperature max', max_digits=5, decimal_places=3, blank=True)),
                ('temperatureMin', models.DecimalField(null=True, verbose_name=b'Temperature min', max_digits=5, decimal_places=3, blank=True)),
                ('quantitePluie', models.DecimalField(verbose_name=b'Quantite de Pluie', max_digits=15, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dateDebut', models.DateField(verbose_name=b'Debut')),
                ('dateFin', models.DateField(verbose_name=b'Fin')),
                ('temperatureMax', models.DecimalField(null=True, verbose_name=b'Temperature max', max_digits=5, decimal_places=3, blank=True)),
                ('temperatureMin', models.DecimalField(null=True, verbose_name=b'Temperature min', max_digits=5, decimal_places=3, blank=True)),
                ('quantitePluie', models.DecimalField(verbose_name=b'Quantite de Pluie', max_digits=15, decimal_places=2, blank=True)),
                ('description', models.TextField(max_length=100, blank=True)),
                ('valider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hauteur', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('nomStation', models.CharField(max_length=45, verbose_name=b'Nom de la Station')),
                ('idStation', models.CharField(max_length=5, blank=True)),
                ('idSiteSeninnelle', models.ForeignKey(verbose_name=b'Site Sentinelle', blank=True, to='base.SiteSentinelle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationObservers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observer', models.OneToOneField(to='base.PersonneContact')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('typeStation', models.CharField(max_length=45, serialize=False, verbose_name=b'Type de Station', primary_key=True)),
                ('description', models.TextField(max_length=100, verbose_name=b'Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uniteMesure', models.CharField(unique=True, max_length=7, verbose_name=b'Unite de mesure')),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(null=True, verbose_name=b'Formule', max_digits=5, decimal_places=3, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(verbose_name=b'Type de la Station', blank=True, to='hydromet.TypeStation', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(verbose_name=b'Unite de mesure', blank=True, to='hydromet.UniteDeMesure', null=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='idStation',
            field=models.ForeignKey(to='hydromet.Station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(default=None, blank=True, to='hydromet.Observation', null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
