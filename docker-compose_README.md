# Projet Cuisine Django - Déploiement Docker

## 📋 Description

Ce projet contient une application Django de gestion de cuisine avec base de données MySQL, containerisée avec Docker pour un déploiement facile sur n'importe quelle machine.

## 🏗️ Architecture

```
Projet_Cuisine_Django/
├── backend/
│   ├── Dockerfile                 # Configuration du conteneur Django
│   ├── docker-compose.yml        # Orchestration des services
│   ├── docker-entrypoint.sh      # Script d'initialisation
│   ├── .dockerignore            # Fichiers exclus de l'image
│   ├── requirements.txt          # Dépendances Python
│   ├── backend/                 # Code Django
│   │   ├── settings.py          # Configuration Django
│   │   └── ...                  # Autres fichiers Django
│   ├── base_donnees/            # Scripts SQL
│   │   └── cuisines_django.sql  # Données initiales
│   └── media/                   # Fichiers médias
└── README_DOCKER.md             # Documentation détaillée
```

## 🚀 Déploiement Rapide

### Prérequis
- Docker Desktop installé
- Git (optionnel)

### 1. Cloner le projet
```bash
git clone <repository-url>
cd Projet_Cuisine_Django/backend
```

### 2. Lancer les conteneurs
```bash
docker-compose up --build
```

### 3. Accéder à l'application
- **Application** : http://localhost:8000
- **Admin Django** : http://localhost:8000/admin
  - Utilisateur: `admin`
  - Mot de passe: `admin123`

### 4. Arrêter
```bash
docker-compose down
```

## 📁 Services Docker

### Web Service (cuisine_web)
- **Image** : Python 3.9-slim personnalisée
- **Port** : 8000
- **Dépendances** : MySQL (db)
- **Volumes** : media/, static/

### Database Service (cuisine_db)
- **Image** : MySQL 8.0
- **Port** : 3306
- **Base de données** : Cuisines_django
- **Volume persistant** : mysql_data

## 🔧 Configuration

### Variables d'environnement
```yaml
environment:
  - DB_HOST=db
  - DB_NAME=Cuisines_django
  - DB_USER=django_user
  - DB_PASSWORD=django_password
  - DB_PORT=3306
```

### Volumes
- `mysql_data` : Persistance des données MySQL
- `./media` : Fichiers uploadés
- `./static` : Fichiers statiques Django

## 🗄️ Base de données

### Initialisation automatique
1. Création de la base de données `Cuisines_django`
2. Import des données depuis `base_donnees/cuisines_django.sql`
3. Exécution des migrations Django
4. Création du superuser (admin/admin123)

### Structure des données
- **Tables principales** : base_cuisines, base_plat, base_utilisateur
- **Tables Django** : auth_user, django_migrations, etc.
- **Données de test** : Plats, cuisines, utilisateurs prédéfinis

## 🛠️ Commandes Utiles

### Logs
```bash
# Voir tous les logs
docker-compose logs

# Logs du service web
docker-compose logs web

# Logs de la base de données
docker-compose logs db
```

### Maintenance
```bash
# Reconstruire les images
docker-compose build --no-cache

# Redémarrer les services
docker-compose restart

# Accéder au conteneur web
docker-compose exec web bash

# Accéder à MySQL
docker-compose exec db mysql -u root -p
```

### Base de données
```bash
# Sauvegarder
docker-compose exec db mysqldump -u root -proot_password Cuisines_django > backup.sql

# Restaurer
docker-compose exec -T db mysql -u root -proot_password Cuisines_django < backup.sql

# Réinitialiser complètement
docker-compose down -v
docker-compose up --build
```

## 🔒 Sécurité

### En production
1. **Changer les mots de passe par défaut**
2. **Utiliser des variables d'environnement sécurisées**
3. **Configurer HTTPS/Nginx**
4. **Limiter les ports exposés**
5. **Utiliser Docker secrets**

### Configuration production suggérée
```yaml
services:
  web:
    environment:
      - DB_HOST=${DB_HOST}
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=0
```

## 🐛 Dépannage

### Problèmes courants

**Port déjà utilisé**
```bash
# Vérifier les ports utilisés
netstat -tulpn | grep :8000
netstat -tulpn | grep :3306

# Changer les ports dans docker-compose.yml
ports:
  - "8001:8000"  # Web
  - "3307:3306"  # MySQL
```

**Base de données inaccessible**
```bash
# Vérifier l'état des conteneurs
docker-compose ps

# Redémarrer uniquement la base de données
docker-compose restart db

# Attendre que MySQL soit prêt
docker-compose logs db
```

**Migration échouée**
```bash
# Exécuter les migrations manuellement
docker-compose exec web python manage.py migrate

# Créer le superuser manuellement
docker-compose exec web python manage.py createsuperuser
```

**Images corrompues**
```bash
# Nettoyer complètement
docker system prune -a
docker-compose down -v
docker-compose up --build
```

## 📊 Monitoring

### Ressources
```bash
# Voir l'utilisation des ressources
docker stats

# Voir l'espace disque utilisé
docker system df
```

### Logs en temps réel
```bash
# Suivre les logs
docker-compose logs -f web
docker-compose logs -f db
```

## 🔄 Mise à jour

### Mettre à jour l'application
```bash
# Récupérer les derniers changements
git pull

# Reconstruire et redémarrer
docker-compose up --build --force-recreate
```

### Mettre à jour les dépendances
```bash
# Mettre à jour requirements.txt
# Puis reconstruire l'image
docker-compose build --no-cache web
```

## 📚 Documentation supplémentaire

- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [MySQL Docker](https://hub.docker.com/_/mysql)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Faire les modifications
4. Tester avec Docker
5. Soumettre une pull request

## 📞 Support

Pour toute question ou problème :
- Vérifier les logs : `docker-compose logs`
- Consulter la documentation : `README_DOCKER.md`
- Créer une issue sur le repository

---

**Développé avec ❤️ et 🐳 Docker**
