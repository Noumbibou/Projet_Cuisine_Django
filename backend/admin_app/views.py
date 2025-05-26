from base.models import Utilisateur
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from base.models import Utilisateur, Commande


class Ingredient_admin(View):
    def get(self, request):
        return render(request, 'ingredient_admin.html', {})

class Commande_admin(View):
    def get(self, request):
        commandes = Commande.objects.select_related('utilisateur').order_by('-id')
        return render(request, 'commande_admin.html', {'commandes': commandes})

class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'base/dashboard.html', {'user': request.user}) 

class Detail_admin(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        utilisateur = Utilisateur.objects.get(pk=request.user.pk)
        return render(request, 'detail_admin.html', {'user': utilisateur})

class Utilisateur_admin(View):
    @method_decorator(login_required)
    def get(self, request):
        utilisateurs = Utilisateur.objects.all()
        return render(request, 'utilisateur_admin.html', {'utilisateurs': utilisateurs})

from base.models import Notification

class NotificationView(View):
    def get(self, request):
        notifications = Notification.objects.select_related('utilisateur').order_by('-date_creation')
        return render(request, 'notification.html', {'notifications': notifications})

from django.http import JsonResponse
from base.models import Notification
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@csrf_exempt
def notification_lu(request, pk):
    if request.method == "POST":
        try:
            notif = Notification.objects.get(pk=pk)
            notif.lu = True
            notif.save()
            return JsonResponse({'success': True})
        except Notification.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Bad request'}, status=400)