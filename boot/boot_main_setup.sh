#!/bin/bash

venv/bin/python manage.py makemigrations

venv/bin/python manage.py migrate

venv/bin/python manage.py createsuperuser --noinput

venv/bin/python manage.py seed ${DJANGO_APP} --number=${SEED_SIZE}

echo "🎉 Starting Django Server ! 🎉"
echo "You can access it at http://localhost:8000/ !"
exec venv/bin/python3 manage.py runserver 0.0.0.0:8000