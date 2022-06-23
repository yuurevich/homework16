from flask import Flask
from migrate import migrate_users, migrate_offers, migrate_orders
from setup_db import db
from flask_restx import Api
from config import Config
from views.offers import offers_ns
from views.orders import orders_ns
from views.users import users_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_app(app)
    return app


def configure_app(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
        api = Api(app)
        api.add_namespace(users_ns)
        api.add_namespace(offers_ns)
        api.add_namespace(orders_ns)
        migrate_users()
        migrate_offers()
        migrate_orders()


if __name__ == '__main__':
    app = create_app(Config)
    app.run(port=5005)
