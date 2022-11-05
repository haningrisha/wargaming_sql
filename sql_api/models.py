from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from utils.serialization import serialize_query
from app import db


class Field(db.Model):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    type = Column(String(50))
    display = Column(String(50))
    query_id = Column(Integer, ForeignKey('queries.id'))
    query = relationship('Query', back_populates='fields')

    def to_dict(self):
        return serialize_query(self)


class Query(db.Model):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    template = Column(Text)
    fields = relationship('Field', back_populates='query')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='queries')

    def to_dict(self):
        ser = serialize_query(self, ['category_id'])
        ser['category'] = self.category.to_dict()
        ser['fields'] = [field.to_dict() for field in self.fields]
        return ser


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    queries = relationship('Query', back_populates='category')

    def to_dict(self):
        return serialize_query(self)
