from flask import request, abort
from flask_login import login_required

from app import app
from sql_api import logic
from . import APP_NAME


@app.route(f'/{ APP_NAME }/queries')
# @login_required
def get_all_queries():
    return logic.get_all_queries()


@app.route(f'/{ APP_NAME }/categories')
# @login_required
def get_categories():
    return logic.get_all_categories()


@app.route(f'/{ APP_NAME }/queries/<category>')
# @login_required
def get_queries_by_category(category: str):
    return logic.get_queries_by_category(category)


@app.route(f'/{ APP_NAME }/execute', methods=['POST'])
# @login_required
def execute_query():
    data: logic.ExecuteRequest = request.json

    try:
        return logic.execute_query(data)
    except ValueError:
        abort(400)


