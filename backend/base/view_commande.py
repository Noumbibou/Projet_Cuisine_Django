from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Commande, Plat, CommandePlat


class CommandeCreateView(View):
    def get(self, request):
        plats = Plat.objects.all()
        return render(request, 'commande_create.html', {'plats': plats})

    def post(self, request):
        utilisateur = request.user
        plat_ids = request.POST.getlist('plats')
        commande = Commande.objects.create(utilisateur=utilisateur)
        for plat_id in plat_ids:
            plat = Plat.objects.get(pk=plat_id)
            CommandePlat.objects.create(commande=commande, plat=plat, quantite=1)
        commande.calculer_prix_total()
        messages.success(request, "Commande créée avec succès.")
        return redirect('commande_list')
    

class CommandeListView(View):
    def get(self, request):
        commandes = Commande.objects.all()
        return render(request, 'commande_list.html', {'commandes': commandes})


class CommandeUpdateView(View):
    def get(self, request, pk):
        commande = Commande.objects.get(pk=pk)
        plats = Plat.objects.all()
        return render(request, 'commande_update.html', {'commande': commande, 'plats': plats})

    def post(self, request, pk):
        commande = Commande.objects.get(pk=pk)
        commande.commandeplat_set.all().delete()  # Supprime les plats existants
        plat_ids = request.POST.getlist('plats')
        for plat_id in plat_ids:
            plat = Plat.objects.get(pk=plat_id)
            CommandePlat.objects.create(commande=commande, plat=plat, quantite=1)
        commande.calculer_prix_total()
        messages.success(request, "Commande mise à jour avec succès.")
        return redirect('commande_list')


class CommandeDeleteView(View):
    def get(self, request, pk):
        commande = Commande.objects.get(pk=pk)
        return render(request, 'commande_delete.html', {'commande': commande})

    def post(self, request, pk):
        commande = Commande.objects.get(pk=pk)
        commande.delete()
        messages.success(request, "Commande supprimée avec succès.")
        return redirect('commande_list')