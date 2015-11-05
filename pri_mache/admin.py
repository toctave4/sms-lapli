from django.contrib import admin

# Register your models here.
from .models import *

class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['nom_produit']

admin.site.register(TypeMarche)
admin.site.register(Marche)
admin.site.register(TypeProduit)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(NiveauOffre)
admin.site.register(ObservationDePrix)


