import os

class Config(object):
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testtokenthatyoullneverguess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT') or 587
    MAIL_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN')
    MAIL_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
    MAIL_SERVER = os.environ.get('MAILGUN_SMTP_SERVER')
   
    GIT_KEY = os.environ.get('GIT_KEY') 

    REDIS_URL = os.environ.get('REDIS_URL')

    