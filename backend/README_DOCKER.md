# Déploiement de l'application Django avec Docker

## Prérequis

- Docker Desktop installé sur votre machine
- Git (si vous clonez le dépôt)

## Instructions de déploiement

### 1. Cloner ou télécharger le projet

```bash
git clone <votre-repo>
cd Projet_Cuisine_Django/backend
```

### 2. Lancer l'application avec Docker Compose

```bash
# Construire et démarrer les conteneurs
docker-compose up --build

# Ou en mode détaché (en arrière-plan)
docker-compose up --build -d
```

### 3. Accéder à l'application

- **Application Django** : http://localhost:8000
- **
- **Admin Django** : http://localhost:8000/admin
  - **Utilisateur** : admin
  - **Mot de passe** : admin123
- **Base de données MySQL** : localhost:3306

### 4. Arrêter l'application

```bash
# Arrêter les conteneurs
docker-compose down

# Arrêter et supprimer les volumes (données)
docker-compose down -v
```

## Structure des conteneurs

- **cuisine_db** : Base de données MySQL 8.0
- **cuisine_web** : Application Django

## Variables d'environnement

Les variables suivantes sont configurées dans docker-compose.yml :

- `DB_HOST` : db (nom du conteneur MySQL)
- `DB_NAME` : Cuisines_django
- `DB_USER` : django_user
- `DB_PASSWORD` : django_password
- `DB_PORT` : 3306

## Volumes persistants

- `mysql_data` : Données de la base de données
- `./media` : Fichiers médias uploadés
- `./static` : Fichiers statiques

## Initialisation automatique

- La base de données est automatiquement créée et peuplée avec `cuisines_django.sql`
- Un superuser Django est créé automatiquement (admin/admin123)
- Les migrations Django sont exécutées automatiquement

## Dépannage

### Vérifier les logs

```bash
# Logs de tous les services
docker-compose logs

# Logs du service web uniquement
docker-compose logs web

# Logs du service base de données
docker-compose logs db
```

### Reconstruire les images

```bash
# Forcer la reconstruction sans cache
docker-compose build --no-cache

# Reconstruire un service spécifique
docker-compose build web
```

### Accéder au conteneur

```bash
# Accéder au conteneur web
docker-compose exec web bash

# Accéder au conteneur de base de données
docker-compose exec db mysql -u root -p
```

### Réinitialiser la base de données

```bash
# Supprimer les volumes et reconstruire
docker-compose down -v
docker-compose up --build
```

## Déploiement en production

Pour un déploiement en production, modifiez le docker-compose.yml :

1. Changez les mots de passe par défaut
2. Ajoutez un reverse proxy (Nginx)
3. Configurez HTTPS avec des certificats SSL
4. Utilisez des variables d'environnement sécurisées
5. Configurez les settings Django pour la production

## Migration des données

Si vous avez des modifications à apporter à la base de données :

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## Sauvegarde et restauration

### Sauvegarder la base de données

```bash
docker-compose exec db mysqldump -u root -proot_password Cuisines_django > backup.sql
```

### Restaurer la base de données

```bash
docker-compose exec -T db mysql -u root -proot_password Cuisines_django < backup.sql
```
