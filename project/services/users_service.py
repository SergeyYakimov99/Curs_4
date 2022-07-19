from typing import Optional

from project.dao.main import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)


    def create(self, user_data):
        """ Создаем нового пользователя с хешированным паролем """
#        user_data['password'] = self.generate_password(user_data['password'])
        password_hash = generate_password_hash(user_data['password'])
        user_data['password'] = password_hash

        self.dao.create(user_data)

    # def generate_password(self, password):
    #     return generate_password_hash(password)

