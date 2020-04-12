release: python manage.py migrate
worker: celery -A team1app worker -l info
web: gunicorn team1app.wsgi