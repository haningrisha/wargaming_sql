import os

from flask import Flask
from jinja2 import Environment, FileSystemLoader
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from main import settings

env = Environment(
    loader=FileSystemLoader(settings.ANGULAR_DIST),
)


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['PLAYGROUND_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'playground.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    return app


app = create_app()
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

