from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
nav = Nav(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app import views, navigation, forms, models, errors, tasks