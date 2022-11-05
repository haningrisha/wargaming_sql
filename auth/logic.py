from typing import TypedDict

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from .models import User, Group
from app import db, login_manager


class LoginData(TypedDict):
    email: str
    password: str


class UserData(LoginData):
    name: str


def _create_user(user_data: UserData):
    return User(
        email=user_data['email'],
        name=user_data['name'],
        password=generate_password_hash(user_data['password'], method='sha256')
    )


def login(login_data: LoginData):
    email = login_data['email']
    password = login_data['password']

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return {
            'error': 'Wrong password or email'
        }

    login_user(user, remember=True)
    return user.to_dict()


def signup(user_data: UserData):
    user = User.query.filter_by(email=user_data['email']).first()

    if user:
        return {
            'error': 'Email address already exists'
        }

    new_user = _create_user(user_data)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()


def logout():
    logout_user()
    return {
        'status': 'Success'
    }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
