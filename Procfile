web: flask db upgrade; gunicorn deploy:app
worker: rq worker -u $REDIS_URL
