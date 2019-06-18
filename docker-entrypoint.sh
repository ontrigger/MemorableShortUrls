#!/bin/bash

echo "collecting static files"
python manage.py collectstatic --noinput

echo "applying database migrations"
python manage.py migrate
