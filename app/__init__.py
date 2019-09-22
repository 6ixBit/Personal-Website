from flask import Flask
from flask_bootstrap import Bootstrap
from Config import Config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

from app import views