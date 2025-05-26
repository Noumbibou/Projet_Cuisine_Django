from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Cuisines(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.SET_NULL, 
        null=True
    )
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def str(self): 
        return self.name
# Create your models here.'''

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email est obligatoire')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=100)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)      
    is_superuser = models.BooleanField(default=False)    

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']
    
    objects = UtilisateurManager()
    
    def str(self):
        return f"{self.prenom} {self.nom}"



# Modèle Plat
class Plat(models.Model):
    image = models.ImageField(upload_to='plats/', null=True, blank=True)
    nom_plat = models.CharField(max_length=100)
    temp_preparation = models.IntegerField(help_text="Temps de préparation en minutes")
    prix = models.DecimalField(max_digits=7, decimal_places=2)
    id_cuisine = models.ForeignKey(Cuisines, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom_plat

# Modèle Ingrédient
class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    quantite = models.CharField(max_length=50)
    id_plat = models.ForeignKey(Plat, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom


# Modèle Catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    id_plat = models.ForeignKey(Plat, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom


# Modèle Historique
class Historique(models.Model):
    date_action = models.DateTimeField(auto_now_add=True)
    type_action = models.CharField(max_length=10, choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')])
    detail = models.TextField()
    id_utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_plat = models.ForeignKey(Plat, on_delete=models.CASCADE, null=True, blank=True)
    id_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return f"{self.type_action} - {self.date_action}"    
    

class Commande(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # L'utilisateur qui passe la commande
    plats = models.ManyToManyField(Plat, through='CommandePlat')  # Relation avec les plats via une table intermédiaire
    date_commande = models.DateTimeField(auto_now_add=True)  # Date de la commande
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Prix total de la commande
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('en_cours', 'En cours'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée')
        ],
        default='en_attente'
    )  # Statut de la commande

    def _str_(self):
        return f"Commande #{self.id_commande} - {self.utilisateur}"

    def calculer_prix_total(self):
        """
        Calcule le prix total de la commande en fonction des plats et des quantités.
        """
        total = 0
        for commande_plat in self.commandeplat_set.all():
            total += commande_plat.plat.prix * commande_plat.quantite
        self.prix_total = total
        self.save()

class PlatArchive(models.Model):
    nom_plat = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='plats_archives/', blank=True, null=True)
    id_cuisine = models.ForeignKey(Cuisines, on_delete=models.CASCADE) # ou ForeignKey si tu veux garder la référence
    temp_preparation = models.CharField(max_length=100, blank=True)
    date_suppression = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_plat

class CommandePlat(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.SET_NULL, null=True, blank=True)
    nom_plat = models.CharField(max_length=255, null=True, blank=True)
    prix_plat = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image_plat = models.ImageField(upload_to='commande_plats/', null=True, blank=True)
    quantite = models.PositiveIntegerField(default=1)
    # ... autres champs utiles

    def save(self, *args, **kwargs):
        if self.plat:
            self.nom_plat = self.plat.nom_plat
            self.prix_plat = self.plat.prix
            self.image_plat = self.plat.image
        super().save(*args, **kwargs)
    

class Notification(models.Model):
    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='notifications'  # Ajoute ceci
    )
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification pour {self.utilisateur.email} - {self.date_creation}"