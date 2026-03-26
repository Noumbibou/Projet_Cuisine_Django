# Guide d'installation - Django Cuisine App

## 🚀 Installation en 3 étapes (2 minutes)

### Étape 1 : Prérequis
1. **Installer Docker Desktop** : https://www.docker.com/products/docker-desktop
2. **Lancer Docker Desktop** (vérifiez que l'icône est active)
3. **Ouvrir un terminal** (PowerShell sur Windows, Terminal sur Mac/Linux)

### Étape 2 : Télécharger et lancer
```bash
# Créer un dossier
mkdir cuisine-django
cd cuisine-django

# Télécharger le fichier de configuration
curl -O https://raw.githubusercontent.com/bidou0204/cuisine-django/main/docker-compose-simple.yml

# Créer les dossiers nécessaires dans le dossier backend
mkdir media static base_donnees

# Lancer l'application (UNE SEULE COMMANDE)
docker-compose -f docker-compose-simple.yml up -d
```

### Étape 3 : Accéder à l'application
- 🌐 **Application** : http://localhost:8000
- 🔐 **Admin** : http://localhost:8000/admin
- 📧 **Email** : admin@example.com
- 🔐 **Mot de passe** : admin123

---

## 🛠️ Commandes utiles

### Vérifier l'état
```bash
docker-compose -f docker-compose-simple.yml ps
```

### Voir les logs
```bash
docker-compose -f docker-compose-simple.yml logs -f
```

### Redémarrer l'application
```bash
docker-compose -f docker-compose-simple.yml restart
```

### Arrêter l'application
```bash
docker-compose -f docker-compose-simple.yml down
```

---

## 🔧 Dépannage

### Si le port 8000 est déjà utilisé
```bash
# Modifier docker-compose-simple.yml
# Changer "8000:8000" en "8001:8000"
```

### Si l'application ne démarre pas
```bash
# Vérifier les logs
docker-compose -f docker-compose-simple.yml logs

# Recréer les conteneurs
docker-compose -f docker-compose-simple.yml down
docker-compose -f docker-compose-simple.yml up -d
```

### Si Docker Desktop n'est pas lancé
1. **Ouvrir Docker Desktop**
2. **Attendre qu'il soit prêt** (icône verte)
3. **Relancer l'application**

---

## 🌐 Accès depuis d'autres appareils

Pour accéder depuis d'autres PC sur le même réseau :
1. **Trouver votre IP locale** :
   - Windows : `ipconfig | findstr "IPv4"`
   - Mac/Linux : `ip addr show | grep inet`

2. **Accéder via l'IP** :
   ```
   http://<VOTRE_IP>:8000
   ```

---

## 📱 Ce que vous obtenez

- ✅ **Application Django complète** avec base de données MySQL
- ✅ **Interface d'administration** fonctionnelle
- ✅ **Données pré-remplies** (cuisines, plats, etc.)
- ✅ **Superuser configuré** automatiquement
- ✅ **Aucune connaissance technique requise**

---

## 🎉 Résultat final

Après 2-3 minutes d'attente, vous aurez une application professionnelle de gestion de cuisine accessible sur votre navigateur !

**C'est aussi simple que ça !** 🚀
