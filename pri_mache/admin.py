from django.contrib import admin

# Register your models here.
from .models import *

class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['nom_produit']

class ObservationDePrixAdmin(admin.ModelAdmin):
    list_display = ("date_collecte", "marche", "produit", "prix", "unitemesure", "observateur", "valider")
    list_filter = ['marche__sectionCommunale__commune__departement', 'marche__sectionCommunale__commune', 'marche__sectionCommunale' , 'marche', 'produit', 'valider']

admin.site.register(TypeMarche)
admin.site.register(Marche)
admin.site.register(TypeProduit)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(ObservationDePrix, ObservationDePrixAdmin)