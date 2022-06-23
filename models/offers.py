from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from setup_db import db


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = relationship('Order')
    executor = relationship('User')


class OfferSchema(Schema):
    id = fields.Int()
    order_id = fields.Int()
    executor_id = fields.Int()
