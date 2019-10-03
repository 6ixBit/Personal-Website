import os

class Config(object):
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or 1

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testtokenthatyoullneverguess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'hamzacarew@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1

    GIT_KEY = os.environ.get('GIT_KEY')

    REDIS_URL = os.environ.get('REDIS_URL')

    