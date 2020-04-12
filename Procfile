release: python manage.py migrate
worker: celery worker --app=team1app
web: gunicorn team1app.wsgi