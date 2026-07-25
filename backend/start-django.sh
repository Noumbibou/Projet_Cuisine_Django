#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."
sleep 30

echo "Starting Django setup..."
python manage.py migrate --noinput

echo "Creating superuser..."
ADMIN_EMAIL="${ADMIN_EMAIL:-admin@example.com}"
ADMIN_PASSWORD="${ADMIN_PASSWORD:-change_this_password}"

python manage.py shell << EOF
from base.models import Utilisateur
if not Utilisateur.objects.filter(email='$ADMIN_EMAIL').exists():
    Utilisateur.objects.create_superuser(
        email='$ADMIN_EMAIL',
        password='$ADMIN_PASSWORD',
        nom='Admin',
        prenom='Super'
    )
    print('Superuser created')
else:
    print('Superuser already exists')
EOF

echo "Starting Django server... si ça demarre lancer l app sur http://localhost:8000"
exec python manage.py runserver 0.0.0.0:8000