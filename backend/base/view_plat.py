from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Commande, Plat, CommandePlat, Cuisines
from django.contrib.auth.decorators import login_required  
from .models import PlatArchive 

class PlatCreateView(View):
    def get(self, request):
        cuisines = Cuisines.objects.all()
        return render(request, 'plat_ajouter.html', {'cuisines': cuisines})

    def post(self, request):
        nom_plat = request.POST.get('nom_plat')
        temp_preparation = request.POST.get('temp_preparation')
        prix = request.POST.get('prix')
        id_cuisine = request.POST.get('id_cuisine')
        cuisine = Cuisines.objects.get(pk=id_cuisine)
        image = request.FILES.get('image')
        Plat.objects.create(
            nom_plat=nom_plat,
            temp_preparation=temp_preparation,
            prix=prix,
            id_cuisine=cuisine,
            image=image
            )# Assurez-vous que le champ 'image' est dans votre formulaire
        messages.success(request, "Plat créé avec succès.")
        return redirect('admin_app:plat')


class PlatDetailView(View):
    def get(self, request, pk):
        plat = Plat.objects.get(pk=pk)
        return render(request, 'plat_detail.html', {'plat': plat})


class PlatListView(View):
    def get(self, request):
        plats = Plat.objects.all()
        return render(request, 'plat_admin.html', {'plats': plats})
    
class PlatUpdateView(View):
    def get(self, request, pk):
        plat = Plat.objects.get(pk=pk)
        cuisines = Cuisines.objects.all()
        return render(request, 'plat_update.html', {'plat': plat, 'cuisines': cuisines})

    def post(self, request, pk):
        plat = Plat.objects.get(pk=pk)
        plat.nom_plat = request.POST.get('nom_plat')
        plat.temp_preparation = request.POST.get('temp_preparation')
        plat.prix = request.POST.get('prix')
        plat.id_cuisine = Cuisines.objects.get(pk=request.POST.get('id_cuisine'))
        # Gestion de l'image
        if request.FILES.get('image'):
            plat.image = request.FILES['image']
        plat.save()
        messages.success(request, "Plat mis à jour avec succès.")
        return redirect('admin_app:plat')


class PlatDeleteView(View):
    def get(self, request, pk):
        try:
            plat = Plat.objects.get(pk=pk)
        except Plat.DoesNotExist:
            messages.error(request, "Ce plat n'existe pas.")
            return redirect('admin_app:plat')
        return render(request, 'plat_delete.html', {'plat': plat})

    def post(self, request, pk):
        try:
            plat = Plat.objects.get(pk=pk)
            PlatArchive.objects.create(
                nom_plat=plat.nom_plat,
                prix=plat.prix,
                image=plat.image,
                id_cuisine=plat.id_cuisine,  # adapte selon ta structure
                temp_preparation=plat.temp_preparation
            )
            plat.delete()
            messages.success(request, "Plat supprimé avec succès.")
        except Plat.DoesNotExist:
            messages.error(request, "Ce plat n'existe pas ou a déjà été supprimé.")
        return redirect('admin_app:plat')
