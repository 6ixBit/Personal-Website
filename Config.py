import os

class Config(object):
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or 1

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgres://nutxlvhtpibzjo:cd5c9be50c8944bc2b76842e4becdb5b3edd9dd9db291a0ef1f9efab47d23baf@ec2-176-34-184-174.eu-west-1.compute.amazonaws.com:5432/ddr1gtuc6chhp3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'realvirtualunity@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1

    GIT_KEY = os.environ.get('GIT_KEY') or '9252928fc441bb25ef40fb2db6f6bfb92042674d'

    REDIS_URL = os.environ.get('REDIS_URL') or "redis://h:p122106cb4c3b8c32eaaddcdfe2113d7c485cf507e82ed14e8e8a5df522ab801c@ec2-34-249-135-201.eu-west-1.compute.amazonaws.com:16439"

    