from flask import send_from_directory

from app import app, env
from . import settings


@app.route('/')
def index():
    tmp = env.get_template('index.html')
    return tmp.render()


@app.route('/auth')
def auth():
    tmp = env.get_template('index.html')
    return tmp.render()


@app.route('/<path:path>')
def load_static(path):
    return send_from_directory(settings.ANGULAR_DIST, path)
