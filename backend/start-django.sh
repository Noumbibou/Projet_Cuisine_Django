#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."
sleep 30

echo "Starting Django setup..."
python manage.py migrate --noinput

echo "Creating superuser..."
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

echo "Starting Django server... si ça demarre lancer l app sur http://localhost:8000"
exec python manage.py runserver 0.0.0.0:8000
