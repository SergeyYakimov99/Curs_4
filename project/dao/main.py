from sqlalchemy import desc
from sqlalchemy.orm import scoped_session

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


# добавил сам

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

    def get_by_email(self, email: str) -> User:
        return self._db_session.query(self.__model__).filter(self.__model__.email == email).first()
