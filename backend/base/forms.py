from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('nom', 'prenom', 'email', 'password1', 'password2')

class ConnexionForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)