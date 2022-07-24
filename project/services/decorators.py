import jwt
from flask import request, abort
from flask import current_app


# def auth_requered(func):
#     """ Декоратор для проверки токена"""
#
#     def wrapper(*args, **kwargs):
#         if 'Authorization' not in request.headers:
#             abort(401)
#
#         token = request.headers['Authorization']
#         try:
#             jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
#         except Exception as e:
#             print(f"JWT decode error {e}")
#             abort(401)
#         return func(*args, **kwargs)
#
#     return wrapper


def auth_requered(func):
    def wrapper(*args, **kwargs):
        access_token = request.cookies.get('AccessToken')

        if not access_token:
            abort(401)

#        data = decode_token(access_token)

        return func(*args, **kwargs)

    return wrapper