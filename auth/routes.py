from flask import request, abort
from flask_login import login_required

from app import app
from . import logic, APP_NAME


@app.route(f'/{ APP_NAME }/login', methods=['POST'])
def login():
    try:
        return logic.login(request.json)
    except ValueError:
        abort(405)


@app.route(f'/{ APP_NAME }/signup', methods=['POST'])
def signup():
    try:
        return logic.signup(request.json)
    except ValueError:
        abort(405)


@app.route(f'/{ APP_NAME }/logout', methods=['GET'])
@login_required
def logout():
    return logic.logout()
