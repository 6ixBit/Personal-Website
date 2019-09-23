from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from Config import Config

app = Flask(__name__)
Bootstrap(app)
nav = Nav(app)
app.config.from_object(Config)

from app import views, navigation