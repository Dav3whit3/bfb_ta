#!/bin/bash

echo '🎉 Making DB migrations ! 🎉'
venv/bin/python manage.py makemigrations

echo '🎉 Migrating DB! 🎉'
venv/bin/python manage.py migrate

echo '🎉 Creating ADMIN superuser ! 🎉'
venv/bin/python manage.py createsuperuser --noinput

echo '🎉 Collecting Statistics for django_import_export ! 🎉'
venv/bin/python manage.py collectstatic --noinput

# [[ -n $SEED_SIZE ]] && venv/bin/python manage.py seed ${DJANGO_APP} --number=${SEED_SIZE}

if [[ -n $SEED_SIZE ]]
 then
  venv/bin/python manage.py seed ${DJANGO_APP} --number=${SEED_SIZE}
 else
  echo "No seed config setup"
fi

echo "🎉 Starting Django Server ! 🎉"
exec venv/bin/python manage.py runserver 0.0.0.0:8000