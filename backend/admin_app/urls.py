from django.urls import path
from . import views
from base.view_plat import PlatCreateView, PlatListView, PlatUpdateView, PlatDeleteView, PlatDetailView
from base.view_commande import CommandeCreateView, CommandeListView, CommandeUpdateView, CommandeDeleteView
from base.views import CuisineListView
from base.view_cuisine import AjouterCuisine
app_name = 'admin_app'
urlpatterns = [
                path('plat/', PlatListView.as_view(), name='plat'),  # Route pour la liste des plats
                path('ingredient/', CuisineListView.as_view(), name='ingredient'),  # Route pour la liste des ingrédients
                path('commande_admin/', views.Commande_admin.as_view(), name='commande_admin'),  # Route pour la liste des catégories
                path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
                path('detail_admin/<int:pk>/', views.Detail_admin.as_view(), name='details_admin'),
                path('utilisateur/', views.Utilisateur_admin.as_view(), name='utilisateur'),  # Redirection vers le dashboard par défaut

                path('plat/ajouter/', PlatCreateView.as_view(), name='ajouter_plat'),
                path('plat/modifier/<int:pk>/', PlatUpdateView.as_view(), name='plat_update'),
                path('plat/supprimer/<int:pk>/', PlatDeleteView.as_view(), name='plat_delete'),
                path('plat/detail/<int:pk>/', PlatDetailView.as_view(), name='plat_detail'),

                path('ingredient/ajouter/', AjouterCuisine.as_view(), name='ajouter_cuisine'),

                path('notification', views.NotificationView.as_view(), name='notifications'),  # Route pour la liste des notifications
                path('notification_lu/<int:pk>/', views.notification_lu, name='notification_lu'),

]
# Create your views here.
