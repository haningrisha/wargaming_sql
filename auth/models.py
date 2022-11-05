from flask_login import UserMixin

from utils.serialization import serialize_query
from app import db

user_group = db.Table('user_group',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('group_name', db.Integer, db.ForeignKey('group.name'))
                      )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    groups = db.relationship('Group', secondary=user_group, backref='users')

    def to_dict(self):
        user = serialize_query(self, exclude=['password'])
        user['groups'] = [group.to_dict() for group in self.groups]
        return user


class Group(db.Model):
    name = db.Column(db.String(100), primary_key=True)

    def to_dict(self):
        return {
            'name': self.name
        }
