from flask import request, abort
from flask_restx import Resource, Namespace
from models.users import UserSchema, User
from setup_db import db

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        user = User.query.all()
        return UserSchema(many=True).dump(user)

    def post(self):
        user = request.json
        db.session.add(User(**user))
        db.session.commit()
        return 'Пользователь добавлен', 201


@users_ns.route('/<id>')
class UserView(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user is None:
            return abort(404)

        return UserSchema().dump(user)

    def put(self, id):
        data = request.json
        data = UserSchema().dump(data)
        User.query.filter(User.id == id).update(data)
        db.session.commit()
        return 'Поля пользователя изменены', 200

    def delete(self, id):
        User.query.filter(User.id == id).delete()
        db.session.commit()
        return 'Пользователь удален', 200