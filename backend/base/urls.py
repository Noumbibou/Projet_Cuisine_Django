from django.urls import path
from . import views
from .ProductDetail import ProductDetail
from .view_commande import CommandeCreateView, CommandeListView, CommandeUpdateView, CommandeDeleteView
from .view_plat import PlatCreateView, PlatListView, PlatUpdateView, PlatDeleteView
from .view_utilisateur import UtilisateurUpdateView, UtilisateurDeleteView
app_name = 'base'
urlpatterns = [
                path('cuisine/', views.CuisineListView.as_view(), name='cuisine_list'),
                path('cuisine/<int:idprod>',ProductDetail.as_view(),name='productsdetail'),

                path('menu/', views.MenuListView.as_view(), name='menu_list'),

                path('Accueil/', views.Accueil.as_view(), name='Accueil'),# Route pour Page d'accueil

                # Route pour commande
                path('commande/', views.CommandeView.as_view(), name='commande'),
                path('cuisine/',ProductDetail.as_view(),name='productsdetail'),
                path('commande/create/', CommandeCreateView.as_view(), name='commande_create'),
                path('commande/list/', CommandeListView.as_view(), name='commande_list'),
                path('commande/update/<int:pk>/', CommandeUpdateView.as_view(), name='commande_update'),
                path('commande/delete/<int:pk>/', CommandeDeleteView.as_view(), name='commande_delete'),
                path('commande/passer_commande/<int:pk>/', views.PasserCommande.as_view(), name='passer_commande'),  # Route pour Détails de la commande
                path('panier/', views.Panier.as_view(), name='valider_panier'),  # Route pour Détails de la commande

                path('panier/valider/', views.enregistrer_commande, name='valider_commande'),  # Route pour Valider le panier

                # Route pour plat

                # Route pour utilisateur
                path('utilisateur/update/<int:pk>/', UtilisateurUpdateView.as_view(), name='utilisateur_update'),
                path('utilisateur/delete/<int:pk>/', UtilisateurDeleteView.as_view(), name='utilisateur_delete'),

                # Route pour Connexion
                path('connexion/', views.Connexion.as_view(), name='connexion'),
                path('inscription/', views.Inscription.as_view(), name='inscription'),
                path('deconnexion/', views.Deconnexion.as_view(), name='deconnexion'),  # Route pour Déconnexion
                path('detail/<int:pk>/', views.Detail.as_view(), name='details_user'),  # Route pour Connexion
    

                #Route concernant l'administration
                    
                path('contact/', views.Contact.as_view(), name='contact'),  # Route pour Contact Us
]