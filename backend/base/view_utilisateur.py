from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from base.models import Utilisateur
from base.forms import InscriptionForm
from django.contrib import messages
from django.views import View

# Détails d'un utilisateur
def utilisateur_detail(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    return render(request, 'utilisateur_detail.html', {'utilisateur': utilisateur})

# Modifier un utilisateur existant
class UtilisateurUpdateView(View):
    def get(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=pk)
        form = InscriptionForm(instance=utilisateur)
        return render(request, 'utilisateur_update.html', {'form': form})

    def post(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=pk)
        form = InscriptionForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, "Utilisateur mis à jour avec succès.")
            return redirect('utilisateur_list')
        return render(request, 'utilisateur_update.html', {'form': form})

# Supprimer un utilisateur
class UtilisateurDeleteView(View):
    def get(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=pk)
        return render(request, 'utilisateur_delete.html', {'utilisateur': utilisateur})

    def post(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=pk)
        utilisateur.delete()
        messages.success(request, "Utilisateur supprimé avec succès.")
        return redirect('utilisateur_list')