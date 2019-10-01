web: flask db upgrade; gunicorn app:app
worker: rq worker -u $REDIS_URL
