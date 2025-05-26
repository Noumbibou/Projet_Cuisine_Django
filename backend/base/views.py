from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib import messages
from .models import Cuisines
from django import forms
from django.contrib.auth import logout
from . cuisine import products
from django.views.decorators.csrf import csrf_exempt
from .models import Utilisateur
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Notification
# Create your views here.

from django.shortcuts import render


class CuisineListView(View):
    def get(self, request):
        cuisine = Cuisines.objects.all()  # Assuming you have a model named Cuisines
        return render(request, 'ingredient_admin.html', {'cuisines':cuisine })

from .models import Plat, Cuisines

class MenuListView(View):
    def get(self, request):
        plats = Plat.objects.all()
        cuisines = Cuisines.objects.all()
        return render(request, 'menu_list.html', {'plats': plats, 'cuisines': cuisines})
    

class Accueil(View):
    def get(self, request):
        return render(request, 'Accueil.html', {'user': request.user}) # Page d'accueil


class CommandeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, "Vous devez être connecté pour voir vos commandes.")
            return redirect('base:connexion')  # ou la page de login de ton projet
        commandes = Commande.objects.filter(utilisateur=request.user).order_by('-id')
        return render(request, 'commande.html', {'commandes': commandes})


from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Plat, Commande

@method_decorator(csrf_exempt, name='dispatch')  # Seulement si vous n'avez pas besoin de CSRF pour cette vue
class Panier(View):
    def post(self, request):
        plats_selectionnes = request.POST.get('plats_selectionnes', '')
        quantites_selectionnees = request.POST.get('quantites_selectionnees', '')

        if not plats_selectionnes or not quantites_selectionnees:
            messages.error(request, "Aucun plat sélectionné.")
            return redirect('base:menu_list')  # Redirige vers la page menu

        plats_ids = plats_selectionnes.split(',')
        quantites = quantites_selectionnees.split(',')

        if len(plats_ids) != len(quantites):
            messages.error(request, "Les données du panier sont invalides.")
            return redirect('base:menu_list')

        # Préparer les données pour l'affichage du panier
        panier = []
        total = 0
        for plat_id, quantite in zip(plats_ids, quantites):
            try:
                plat = Plat.objects.get(id=int(plat_id))
                quantite = int(quantite)
                sous_total = plat.prix * quantite
                total += sous_total
                panier.append({
                    'plat': plat,
                    'quantite': quantite,
                    'sous_total': sous_total
                })
            except (Plat.DoesNotExist, ValueError):
                continue

        return render(request, 'panier.html', {
            'panier': panier,
            'total': total
        })


from .models import Commande, CommandePlat, Plat

def enregistrer_commande(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Vous devez être connecté pour valider votre commande.")
            return redirect('base:panier')  # ou la page panier/menu selon ton besoin

        plats_ids = request.POST.getlist('plats_ids')
        quantites = request.POST.getlist('quantites')

        commande = Commande.objects.create(utilisateur=request.user)
        lignes = []
        for plat_id, quantite in zip(plats_ids, quantites):
            plat = Plat.objects.get(id=plat_id)
            ligne = CommandePlat.objects.create(
                commande=commande,
                plat=plat,
                nom_plat=plat.nom_plat,
                prix_plat=plat.prix,
                image_plat=plat.image,
                quantite=int(quantite),
            )
            # Calcul du sous-total pour cette ligne
            sous_total = plat.prix * ligne.quantite
            # Ajoute le sous-total comme attribut à l'objet ligne pour le template
            ligne.sous_total = sous_total
            lignes.append(ligne)
        commande.calculer_prix_total()
        return render(request, 'commande_success.html', {
            'commande': commande,
            'lignes': lignes
        })
    return redirect('base:menu_list')

class PasserCommande(View):
    def post(self, request, pk):
        plat = Plat.objects.get(pk=pk)
        quantite = int(request.POST.get('quantite', 1))
        sous_total = plat.prix * quantite
        panier = [{
            'plat': plat,
            'quantite': quantite,
            'sous_total': sous_total
        }]
        total = sous_total
        return render(request, 'panier.html', {
            'panier': panier,
            'total': total,
            'is_single': True  # Pour différencier dans le template si besoin
        })
    
class Connexion(View):
    def get(self, request):
        return render(request, 'connexion.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_app:commande_admin')
            else:
                return redirect('base:Accueil')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
            return render(request, 'connexion.html')

from .models import Notification

class Contact(View):        
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        email = request.POST.get('email')
        message = request.POST.get('message')
        success = False
        error = None
        if email and message:
            Notification.objects.create(
                utilisateur=request.user if request.user.is_authenticated else None,
                message=message,
                lu=False,
            )
            success = True
        else:
            error = "Veuillez remplir tous les champs."
        return render(request, 'contact.html', {
            'success': success,
            'error': error,
            'request': request
        }) 


class Inscription(View):
    def get(self, request):
        form = InscriptionForm()
        return render(request, 'inscription.html', {'form': form})

    def post(self, request):
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Supprimez login(request, user) pour ne pas connecter automatiquement
            messages.success(request, "Inscription réussie ! Veuillez vous connecter.")
            return redirect('base:connexion')  # Redirection vers la page de connexion
        return render(request, 'inscription.html', {'form': form})

class Deconnexion(View):
    @method_decorator(require_POST)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Déconnexion réussie !")
        return redirect('base:Accueil')

# Page Dashboard   
class Detail(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=request.user.pk)
        return render(request, 'detail_user.html', {'utilisateur': utilisateur})