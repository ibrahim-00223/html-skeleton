#!/bin/bash

# Appliquer les migrations Django
echo "Applying Django migrations..."
python manage.py migrate

# Démarrer le serveur Django
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000