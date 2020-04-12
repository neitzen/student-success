release: python manage.py migrate
worker: celery worker -A team1app worker
web: gunicorn gettingstarted.wsgi