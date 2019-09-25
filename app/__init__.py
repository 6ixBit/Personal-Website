from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Config import Config

app = Flask(__name__)
Bootstrap(app)
nav = Nav(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object(Config)

from app import views, navigation, forms, models