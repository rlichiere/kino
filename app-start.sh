#!/bin/bash

set -e

# Migrate DB
python manage.py migrate

# Create Super User
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')" | python manage.py shell

#Copy Static FIles
python manage.py collectstatic --noinput

#Run Provisioning APP
exec python manage.py runserver 0.0.0.0:8000
