import jwt
from flask import request, abort
#from constants import secret, algo


secret = "SECRET_KEY"
algo = 'HS256'

def auth_requered(func):
    """ Декоратор на авторизацию"""

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        token = request.headers['Authorization']
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print(f"JWT decode error {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper
