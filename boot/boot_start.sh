#!/bin/bash

echo '🎉 Collecting Statistics for django_import_export ! 🎉'
venv/bin/python3 manage.py collectstatic --noinput

echo "🎉 Starting Django Server ! 🎉"
echo "You can access it at http://localhost:8000/ !"
exec venv/bin/python3 manage.py runserver 0.0.0.0:8000