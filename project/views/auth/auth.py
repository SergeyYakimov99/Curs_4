from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service


api = Namespace('auth')


@api.route('/register/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email")
        password = req_json.get("password")
        if not (email or password):
            return "необходимо ввести логин и пароль", 400

        # создаем пользователя в системе

        user_service.create(req_json)
        return 201


@api.route('/login/')
class AuthView(Resource):
    """ передаем email и пароль и, если пользователь прошел аутентификацию,
    возвращаем пользователю ответ в виде двух токенов. """
    def post(self):
        req_json = request.json
        email = req_json.get("email")
        password = req_json.get("password")
        if not (email or password):
            return "необходимо ввести логин и пароль", 400
        token_two = auth_service.generate_tokens(email, password)
        return token_two


    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        token_two = auth_service.approve_refresh_token(token)
        return token_two

# - принимаем пару токенов и, если они валидны, создаем пару новых.
 # На данном этапе нужно обязательно проверить работу механизма аутентификации через Postman
    # (или используйте любой другой инструмент)

