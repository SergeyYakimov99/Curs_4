import base64
import hashlib
import hmac

from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
# декодируем пароль из хеша
def compare_passwords(password_bd, password_inp):
    password_inp = generate_password_hash(password_inp)
    return hmac.compare_digest(password_bd, password_inp)

