import calendar
import datetime

from project.dao import UsersDAO
from project.exceptions import BaseServiceError, ItemNotFound
from project.tools.security import compare_passwords

from flask import current_app

import jwt

from project.services.users_service import UsersService

SECRET_KEY = "SECRET_KEY"
algo = 'HS256'


# SECRET_KEY = current_app.config["SECRET_KEY"]
# algo = current_app.config["ALGORITHM"]

class AuthService:
    def __init__(self, user_dao: UsersDAO):
        self.user_dao = user_dao

    def generate_tokens(self, email, password):
        user = self.user_dao.get_by_email(email)

        if not user:
            raise ItemNotFound("Нет такого пользователя")

        if not compare_passwords(password_inp=password, password_bd=user.password):
            raise BaseServiceError("Введен неверный пароль")

        data = {
            "email": user.email,
            "password": user.password
        }
        # генерируем access_token на 30 мин.
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=algo)

        # генерируем refresh_token на 130 дней.
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=algo)

        return {"access_token": access_token, "refresh_token": refresh_token}, 201

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, SECRET_KEY, algorithms=[algo])
        email = data['email']
        user = self.user_dao.get_by_email(email)

        if not user:
            return False

        return self.generate_tokens(email)
