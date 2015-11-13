# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commune', models.CharField(unique=True, max_length=45, verbose_name=b'Commune')),
                ('description', models.TextField(max_length=100, verbose_name=b'Description', blank=True)),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name=b'Code')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departement', models.CharField(max_length=40, verbose_name=b'Departement')),
                ('description', models.TextField(max_length=100, verbose_name=b'Description', blank=True)),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name=b'Code')),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomPersonne', models.CharField(max_length=45, verbose_name=b'Nom')),
                ('prenomPersonne', models.CharField(max_length=45, verbose_name=b'Prenom')),
                ('telephoneBureau', models.CharField(max_length=45, verbose_name=b'Telephone (Bureau)', blank=True)),
                ('telephonePersonnel', models.CharField(unique=True, max_length=45, verbose_name=b'Telephone (Personnel)')),
                ('emailPersonnel', models.CharField(max_length=45, verbose_name=b'Email (Personnel)', blank=True)),
                ('adressePersonnelle', models.CharField(max_length=45, verbose_name=b'Adresse (Personnlle)', blank=True)),
                ('nif', models.CharField(unique=True, max_length=45, verbose_name=b'NIF/CIN')),
                ('dateEmbauche', models.DateField(verbose_name=b"Date d'embauche")),
                ('isactif', models.BooleanField(verbose_name=b'Active')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(max_length=45, unique=True, serialize=False, verbose_name=b'Poste', primary_key=True)),
                ('description', models.CharField(max_length=45, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sectionCommunale', models.CharField(max_length=45, verbose_name=b'Section Communale')),
                ('nomOfficiel', models.CharField(max_length=45, verbose_name=b'Nom officiel', blank=True)),
                ('description', models.TextField(max_length=100, verbose_name=b'Description', blank=True)),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name=b'Code')),
                ('commune', models.ForeignKey(verbose_name=b'Commune', to='base.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localite', models.CharField(max_length=45, verbose_name=b'Localite')),
                ('latitude', models.DecimalField(default=0, verbose_name=b'Latitude', max_digits=8, decimal_places=2)),
                ('longitude', models.DecimalField(default=0, verbose_name=b'Longitude', max_digits=8, decimal_places=2)),
                ('hauteur', models.DecimalField(default=0, verbose_name=b'Hauteur', max_digits=8, decimal_places=2)),
                ('sectionCommunale', models.ForeignKey(verbose_name=b'Section Communale', to='base.SectionCommunale')),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(verbose_name=b'Poste', to='base.Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(verbose_name=b'Departement', to='base.Departement'),
        ),
    ]
