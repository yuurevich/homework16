from data import users, orders, offers
from models.users import User
from models.offers import Offer
from models.orders import Order
from setup_db import db
from datetime import datetime


def migrate_users():
    new_users = []
    for user in users:
        new_users.append(User(**user))
    with db.session.begin():
        db.session.add_all(new_users)


def migrate_offers():
    new_offers = []
    for offer in offers:
        new_offers.append(Offer(**offer))

    with db.session.begin():
        db.session.add_all(new_offers)


def migrate_orders():
    new_orders = []
    for order in orders:
        order['start_date'] = datetime.strptime(order['start_date'], '%m/%d/%Y')
        order['end_date'] = datetime.strptime(order['end_date'], '%m/%d/%Y')
        new_orders.append(Order(**order))
    with db.session.begin():
        db.session.add_all(new_orders)