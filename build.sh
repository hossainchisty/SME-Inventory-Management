#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python -m pip install --upgrade pip
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperman