release: python manage.py migrate
web: gunicorn team1app.wsgi
worker: celery worker -A team1app worker