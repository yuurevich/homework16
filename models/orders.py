from sqlalchemy.orm import relationship
from setup_db import db
from marshmallow import Schema, fields


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(255))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    costumer = relationship('User', foreign_keys='Order.customer_id')
    executor = relationship('User', foreign_keys='Order.executor_id')


class OrderSchema(Schema):
    id = fields.Int()
    description = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()
    address = fields.Str()
    price = fields.Int()
    customer_id = fields.Int()
    executor_id = fields.Int()
