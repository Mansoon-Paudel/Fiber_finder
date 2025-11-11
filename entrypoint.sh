#!/usr/bin/env bash
set -e

# install any additional build steps if necessary (optional)
# run migrations
python manage.py migrate --noinput

# collect static files
python manage.py collectstatic --noinput

# start gunicorn
exec gunicorn foodie.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --log-level info
