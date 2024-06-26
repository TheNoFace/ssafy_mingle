#!/bin/sh

# django-admin startproject mysite .
sed -i 's/ALLOWED_HOSTS = \[]/ALLOWED_HOSTS = \["*"]/g' movie_recommend/settings.py
python manage.py migrate
python manage.py loaddata movies_fixtures.json accounts_fixtures.json
