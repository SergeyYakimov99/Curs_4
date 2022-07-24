from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
from project.services.decorators import auth_requered
from project.setup.api.models import user


api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @auth_requered  # декоратор на просмотр профиля
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.get_user_by_token(refresh_token=header)

    @auth_requered  # декоратор на изменение профиля
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def patch(self):
        """ изменяет информацию пользователя (имя, фамилия, любимый жанр)"""
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.update_user(data=data, refresh_token=header)


@api.route('/password/')
class UserView(Resource):
 #   @auth_requered  # декоратор на замену пароля
    def put(self):
        """ обновляет пароль пользователя, для этого нужно отправить два пароля password_1 и password_2"""

        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_password(data=data, refresh_token=header)
