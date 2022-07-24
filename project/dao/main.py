from sqlalchemy import desc
from sqlalchemy.orm import scoped_session

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User
from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def __init__(self, db_session: scoped_session) -> None:
        super().__init__(db_session)

    # сортировка фильмов по годам, начиная с самого "свежего"

    def get_by_new_year(self):
        return self._db_session.query(self.__model__).order_by(desc(self.__model__.year)).all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def __init__(self, db_session: scoped_session) -> None:
        super().__init__(db_session)

    def get_by_email(self, login):
        try:
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == login).one()
            return stmt
        except Exception as e:
            print(e)
            return {}

    def create(self, login, password):
        """
        Добавляем нового пользователя в БД
        """

        try:
            self._db_session.add(
                User(
                    email=login,
                    password=generate_password_hash(password)
                )
            )
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def update(self, login, data):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == login).update(
                data
            )
            self._db_session.commit()
            print("Пользователь обновлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()
