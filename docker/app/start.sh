#!/usr/bin/env sh

make migrate

python manage.py runserver 0.0.0.0:8000
