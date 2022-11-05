from flask import request, abort
from flask_login import login_required

from app import app
from auth import group_member
from . import APP_NAME
from . import logic


@app.route(f'/{ APP_NAME }/query', methods=['PUT'])
@login_required
@group_member('admin')
def create_query():
    data: logic.QueryRequest = request.json
    try:
        return logic.add_query(data)
    except ValueError:
        abort(405)


@app.route(f'/{ APP_NAME }/query/<int:query_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
@group_member('admin')
def change_query(query_id: int):
    if request.method == 'GET':
        return logic.get_query(query_id)

    if request.method == 'DELETE':
        return logic.delete_query(query_id)

    if request.method == 'PUT':
        return logic.update_query(query_id)
