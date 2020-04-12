release: python manage.py migrate
worker: celery worker -A team1app worker
web: gunicorn team1app.wsgi