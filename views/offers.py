from flask import request, abort
from flask_restx import Resource, Namespace
from models.offers import OfferSchema, Offer
from setup_db import db

offers_ns = Namespace('offers')


@offers_ns.route('/')
class OffersView(Resource):
    def get(self):
        offer = Offer.query.all()
        return OfferSchema(many=True).dump(offer)

    def post(self):
        offer = request.json
        db.session.add(Offer(**offer))
        db.session.commit()
        return 'Предложение добавлено', 201


@offers_ns.route('/<id>')
class offerView(Resource):
    def get(self, id):
        offer = Offer.query.get(id)
        if offer is None:
            return abort(404)

        return OfferSchema().dump(offer)

    def put(self, id):
        data = request.json
        data = OfferSchema().dump(data)
        Offer.query.filter(Offer.id == id).update(data)
        db.session.commit()
        return 'Поля предложения изменены', 200

    def delete(self, id):
        Offer.query.filter(Offer.id == id).delete()
        db.session.commit()
        return 'Предложение удалено', 200