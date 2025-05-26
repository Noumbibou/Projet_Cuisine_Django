from django.contrib import admin

from .models import Utilisateur, UtilisateurManager, Cuisines, Ingredient, Commande, CommandePlat, Plat
admin.site.register(Utilisateur)
admin.site.register(Ingredient)
admin.site.register(Plat)
admin.site.register(Commande)
admin.site.register(CommandePlat)
admin.site.register(Cuisines)
# Register your models here.
