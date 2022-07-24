from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register/')
class AuthView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create(data.get('email'), data.get('password')), 201
        else:
            return "ВВедите email и password", 401


@api.route('/login/')
class AuthView(Resource):
    """ передаем email и пароль и, если пользователь прошел аутентификацию,
    возвращаем пользователю ответ в виде двух токенов. """

    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.check(data.get('email'), data.get('password')), 201
        else:
            return "необходимо ввести логин и пароль", 400

    @api.response(404, 'Not Found')
    def put(self):
        # - принимаем пару токенов и, если они валидны, создаем пару новых.

        data = request.json
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201
        else:
            return "Чего то не хватает", 401
