# Cuisine Projet

## 📋 Présentation

Cette application est une plateforme de gestion de cuisine permettant :
- La gestion des plats, ingrédients, commandes et utilisateurs.
- Un espace administrateur pour gérer les notifications, les utilisateurs, les plats et les commandes.
- Un formulaire de contact qui enregistre les messages comme notifications pour l'admin.

## 🐳 Installation avec Docker (recommandé)

### Prérequis
- Docker et Docker Compose installés ([Docker Desktop](https://www.docker.com/products/docker-desktop) sur Windows/Mac, ou Docker Engine + plugin Compose sur Linux)

### Démarrage

1. **Cloner le projet :**
```bash
   git clone https://github.com/Noumbibou/Projet_Cuisine_Django.git
   cd Projet_Cuisine_Django/backend
```

2. **Lancer l'application :**
```bash
   docker compose up --build
```

   Cette commande construit l'image Django, démarre MySQL, importe automatiquement les données de démonstration, applique les migrations, et crée un superuser.

3. **Accéder à l'application :**
   - 🌐 Application : http://localhost:8000
   - 🔐 Admin Django : http://localhost:8000/admin/
   - 📧 Email superuser par défaut : `admin@example.com`
   - 🔑 Mot de passe par défaut : `change_this_password_now`

   *(Ces identifiants par défaut sont définis dans `docker-compose.yml` via les variables `ADMIN_EMAIL` / `ADMIN_PASSWORD` — modifie-les avant un usage autre que local/démo.)*

### Commandes utiles

```bash
# Voir l'état des conteneurs
docker compose ps

# Voir les logs en direct
docker compose logs -f

# Arrêter l'application
docker compose down

# Arrêter et repartir de zéro (supprime aussi les données de la base)
docker compose down -v
```

### Dépannage

**Le port 8000 ou 3307 est déjà utilisé**
Modifie le port exposé dans `docker-compose.yml`, par exemple `"8001:8000"` au lieu de `"8000:8000"`.

**L'application ne démarre pas**
```bash
docker compose logs
docker compose down -v
docker compose up --build
```

**Identifiants admin qui ne fonctionnent pas**
Vérifie que l'email défini dans `ADMIN_EMAIL` (dans `docker-compose.yml`) n'entre pas en conflit avec un utilisateur déjà présent dans `base_donnees/cuisines_django.sql`.

## 🛠️ Installation manuelle (sans Docker)

1. Créer un environnement virtuel Python :
```bash
   python -m venv venv
   source venv/bin/activate  # Windows : venv\Scripts\activate
```
2. Installer les dépendances :
```bash
   pip install -r backend/requirements.txt
```
3. Configurer une base MySQL locale et les variables d'environnement (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY`).
4. Appliquer les migrations et lancer le serveur :
```bash
   python manage.py migrate
   python manage.py runserver
```

## 📱 Fonctionnalités

- ✅ Gestion complète des plats, ingrédients et commandes
- ✅ Espace administrateur (notifications, utilisateurs, plats, commandes)
- ✅ Formulaire de contact relié aux notifications admin
- ✅ Données de démonstration pré-remplies au premier lancement
- ✅ Superuser configuré automatiquement au démarrage