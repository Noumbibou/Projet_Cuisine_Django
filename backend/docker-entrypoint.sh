#!/bin/bash
set -e

# Attendre un peu que MySQL soit complètement prêt
echo "Waiting for MySQL to be ready..."
sleep 30

echo "Starting Django setup..."

# Lancer les migrations Django
python manage.py migrate --noinput

# Créer un superuser si nécessaire
python manage.py shell << EOF
from base.models import Utilisateur
if not Utilisateur.objects.filter(email='admin@example.com').exists():
    Utilisateur.objects.create_superuser(
        email='admin@example.com',
        password='admin123',
        nom='Admin',
        prenom='Super'
    )
    print('Superuser created')
else:
    print('Superuser already exists')
EOF

# Lancer le serveur Django
exec "$@"
