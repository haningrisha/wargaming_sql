from typing import TypedDict, List
from app import app, db

from sql_api.models import Query, Category, Field


class Parameters(TypedDict):
    code: str
    type: str
    display: str


class QueryRequest(TypedDict):
    name: str
    description: str
    category_id: int
    template: str
    parameters: List[Parameters]


def _create_query(qr, category):
    return Query(
        name=qr['name'],
        description=qr['description'],
        template=qr['template'],
        category=category
    )


def _create_field(field_data, query):
    return Field(
        code=field_data['code'],
        type=field_data['type'],
        display=field_data['display'],
        query=query
    )


def add_query(qr: QueryRequest):
    with app.app_context():
        category = Category.query.get(qr['category_id'])
        query = _create_query(qr, category)
        db.session.add(query)
        for field_data in qr['parameters']:
            field = _create_field(field_data, query)
            db.session.add(field)
        db.session.commit()
        return query.to_dict()


def get_query(query_id: int):
    with app.app_context():
        query = Query.query.get(query_id)
        return query.to_dict()


def delete_query(query_id: int):
    with app.app_context():
        Query.query.filter_by(id=query_id).delete()
        db.session.commit()
        return {
            'status': 'Success'
        }


def update_query(query_id: int):
    raise NotImplemented
