from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TypeMarche)
admin.site.register(Marche)
admin.site.register(TypeProduit)
admin.site.register(Produit)
admin.site.register(NiveauOffre)
admin.site.register(ObservationDePrix)


