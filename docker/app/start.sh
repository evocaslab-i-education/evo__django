#!/usr/bin/env sh

#python manage.py migrate
make migrate

python manage.py runserver 0.0.0.0:8000
