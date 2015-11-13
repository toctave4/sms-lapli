# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('hydromet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_marche', models.CharField(max_length=45, verbose_name=b'Marche')),
                ('latitude', models.DecimalField(default=0, verbose_name=b'Latitude', max_digits=8, decimal_places=2)),
                ('longitude', models.DecimalField(default=0, verbose_name=b'Longitude', max_digits=8, decimal_places=2)),
                ('hauteur', models.DecimalField(default=0, verbose_name=b'Hauteur', max_digits=8, decimal_places=2)),
                ('siteSentinelle', models.ForeignKey(verbose_name=b'Site sentinelle', to='base.SiteSentinelle')),
            ],
        ),
        migrations.CreateModel(
            name='NiveauOffre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau_offre', models.CharField(max_length=45, verbose_name=b"Niveau de l'offre")),
                ('description', models.TextField(max_length=150, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='ObservationDePrix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_collecte', models.DateTimeField(verbose_name=b'Date collecte de donnees')),
                ('prix', models.DecimalField(default=0, verbose_name=b'Prix', max_digits=8, decimal_places=2)),
                ('marche', models.ForeignKey(verbose_name=b'Marche', to='pri_mache.Marche')),
            ],
            options={
                'verbose_name_plural': 'Observations de prix',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_produit', models.CharField(max_length=45, verbose_name=b'Code Produit')),
                ('nom_produit', models.CharField(max_length=45, verbose_name=b'Nom Produit')),
                ('marque', models.CharField(max_length=45, verbose_name=b'Marque')),
                ('origine', models.CharField(max_length=45, verbose_name=b'Origine')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMarche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_marche', models.CharField(max_length=45, verbose_name=b'Type Marche')),
                ('description', models.TextField(max_length=150, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_produit', models.CharField(max_length=45, verbose_name=b'Type Produit')),
                ('description', models.TextField(max_length=150, verbose_name=b'Description')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='type_produit',
            field=models.ForeignKey(verbose_name=b'Type Produit', to='pri_mache.TypeProduit'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='produit',
            field=models.ForeignKey(verbose_name=b'Produit', to='pri_mache.Produit'),
        ),
        migrations.AddField(
            model_name='observationdeprix',
            name='unitemesure',
            field=models.ForeignKey(verbose_name=b'Unite de mesure', to='hydromet.UniteDeMesure'),
        ),
        migrations.AddField(
            model_name='marche',
            name='type_marche',
            field=models.ForeignKey(verbose_name=b'Type Marche', to='pri_mache.TypeMarche'),
        ),
    ]
