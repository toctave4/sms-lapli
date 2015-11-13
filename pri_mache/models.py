from django.db import models
from base.models import SiteSentinelle, PersonneContact, SectionCommunale
from hydromet.models import UniteDeMesure

# Create your models here.

#  -------------------------------------------
#  Models for this app
#  -------------------------------------------
class TypeMarche(models.Model):
    type_marche=models.CharField(max_length=45, verbose_name="Type Marche")
    description=models.TextField(max_length=150,verbose_name="Description")

    def __str__(self):
        return self.type_marche

class Marche(models.Model):
    nom_marche=models.CharField(max_length=45, verbose_name="Marche")
    latitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Longitude")
    hauteur = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Hauteur")
    type_marche=models.ForeignKey(TypeMarche,verbose_name="Type Marche")
    sectionCommunale=models.ForeignKey(SectionCommunale, verbose_name="Section Communale", null=True)
    #siteSentinelle=models.ForeignKey(SiteSentinelle, verbose_name="Site sentinelle")
    def __str__(self):
        return self.nom_marche

class TypeProduit(models.Model):
    type_produit=models.CharField(max_length=45, verbose_name="Type Produit")
    description=models.TextField(max_length=150, verbose_name="Description")

    def __str__(self):
        return self.type_produit


class Produit(models.Model):
    code_produit=models.CharField(max_length=45, verbose_name="Code Produit")
    nom_produit=models.CharField(max_length=45,verbose_name="Nom Produit")
    marque=models.CharField(max_length=45, verbose_name="Marque")
    origine=models.CharField(max_length=45,verbose_name="Origine")
    type_produit=models.ForeignKey(TypeProduit, verbose_name="Type Produit")

    def __str__(self):
        return self.nom_produit


class NiveauOffre(models.Model):
    niveau_offre=models.CharField(max_length=45, verbose_name="Niveau de l'offre")
    description=models.TextField(max_length=150, verbose_name="Description")

    def __str__(self):
        return self.niveau_offre


class ObservationDePrix(models.Model):
    date_collecte=models.DateTimeField(auto_now_add=True, verbose_name="Date collecte de donnees")
    prix=models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix")
    marche=models.ForeignKey(Marche, verbose_name="Marche")
    produit=models.ForeignKey(Produit, verbose_name="Produit")
    unitemesure=models.ForeignKey(UniteDeMesure, verbose_name="Unite de mesure")
    observateur=models.ForeignKey(PersonneContact, null=True)
    description=models.TextField(max_length=100, blank=True)
    valider=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Observations de prix"

    @property
    def log(self):
        return Log.objects.filter(observation=self.pk).count()


class Log(models.Model):
    observation = models.ForeignKey(ObservationDePrix, null=True, blank=True, default = None)
    collecteur = models.ForeignKey(PersonneContact, verbose_name="Collecteur", related_name='collecteur')
    date_collecte = models.DateTimeField(auto_now_add=True)
    prix=models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Prix")
    marche=models.ForeignKey(Marche, verbose_name="Marche")
    produit=models.ForeignKey(Produit, verbose_name="Produit")
    unitemesure=models.ForeignKey(UniteDeMesure, verbose_name="Unite de mesure")

    def __str__(self):              # __unicode__ on Python 2
        return self.collecteur.nomPersonne + ' ' + self.collecteur.prenomPersonne
