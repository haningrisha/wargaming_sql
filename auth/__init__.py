from functools import wraps

from flask_login import current_user
from flask import abort


APP_NAME = 'auth'


def group_member(group: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_groups = [gp.name for gp in current_user.groups]
            if group not in user_groups:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
