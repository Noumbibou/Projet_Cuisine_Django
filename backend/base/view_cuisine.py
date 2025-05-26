from .models import Cuisines
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

class AjouterCuisine(View):
    def get(self, request):
        return render(request, 'ajouter_cuisine.html')

    def post(self, request):
        nom_cuisine = request.POST.get('nom_cuisine')
        description = request.POST.get('description')
        if nom_cuisine:
            # Vérifie si une cuisine avec ce nom existe déjà (insensible à la casse)
            if Cuisines.objects.filter(name__iexact=nom_cuisine).exists():
                messages.error(request, "Ce nom de cuisine existe déjà.")
                return render(request, 'ajouter_cuisine.html')
            Cuisines.objects.create(name=nom_cuisine, description=description)
            messages.success(request, "Cuisine ajoutée avec succès.")
            return redirect('admin_app:ingredient')  # Redirige vers la page appropriée
        else:
            messages.error(request, "Le nom de la cuisine est requis.")
            return render(request, 'ajouter_cuisine.html')