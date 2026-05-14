#!/bin/bash

# Appliquer les migrations Django
echo "Applying Django migrations..."
python3 manage.py migrate

# Démarrer le serveur Django
echo "Starting Django server..."
python3 manage.py runserver 0.0.0.0:8000