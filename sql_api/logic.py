from typing import TypedDict, Union, List
import datetime

import jinja2
from sqlalchemy import exc

from sql_api.models import Query, Category
from playground.playground import playground
from utils.database_utils import create_table


class Parameter(TypedDict):
    code: str
    value: Union[str, datetime.datetime, int]


class ExecuteRequest(TypedDict):
    query_id: int
    parameters: List[Parameter]


def get_all_queries():
    queries = Query.query.all()
    return [query.to_dict() for query in queries]


def get_all_categories():
    categories = Category.query.all()
    return [category.to_dict() for category in categories]


def get_queries_by_category(category_name: str):
    category = Category.query.filter_by(name=category_name).first()
    queries = Query.query.filter_by(category=category)
    return [query.to_dict() for query in queries]


def validate_fields(query: Query, params: List[Parameter]) -> bool:
    required_codes = {field.code for field in query.fields}
    received_field = {param.get('code') for param in params}

    return (required_codes ^ received_field) == set()


def _format_template(template, fields):
    env = jinja2.Environment()
    template = env.from_string(template)
    return template.render(**{
        param.get('code'): param.get('value') for param in fields
    })


def execute_query(execute_request: ExecuteRequest):
    template_id = execute_request.get('query_id')
    query = Query.query.get(template_id)
    template = query.template
    parameters = execute_request.get('parameters')

    if not validate_fields(query, parameters):
        raise ValueError

    statement = _format_template(template, parameters)

    with playground.connect() as connection:
        try:
            result = connection.execute(statement).fetchall()
        except exc.OperationalError as exception:
            return {
                "error": exception.orig.args[0]
            }

    return create_table(result)
