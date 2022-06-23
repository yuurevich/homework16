from flask import request, abort
from flask_restx import Resource, Namespace
from models.orders import OrderSchema, Order
from setup_db import db

orders_ns = Namespace('orders')


@orders_ns.route('/')
class OrdersView(Resource):
    def get(self):
        order = Order.query.all()
        return OrderSchema(many=True).dump(order)

    def post(self):
        order = request.json
        db.session.add(order(**order))
        db.session.commit()
        return 'Заказ добавлен', 201


@orders_ns.route('/<id>')
class OrderView(Resource):
    def get(self, id):
        order = Order.query.filter(Order.id == id).first()
        if order is None:
            return abort(404)

        return OrderSchema().dump(order)

    def put(self, id):
        data = request.json
        data = OrderSchema().dump(data)
        Order.query.filter(Order.id == id).update(data)
        db.session.commit()
        return 'Поля заказа изменены', 200

    def delete(self, id):
        Order.query.filter(Order.id == id).delete()
        db.session.commit()
        return 'Заказ удален', 200