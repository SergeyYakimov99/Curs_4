from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genre'

    name = Column(String(100), unique=True, nullable=False)


# добавил сам

class Director(models.Base):
    __tablename__ = 'director'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer(), nullable=False)
    rating = Column(Float(), nullable=False)
    genre_id = Column(Integer(), ForeignKey('genre.id'), nullable=False)
    genre = relationship('Genre', foreign_keys=genre_id)   # ???
    director_id = Column(Integer(), ForeignKey('director.id'), nullable=False)
    director = relationship('Director', foreign_keys=director_id)  # ???


class User(models.Base):
    __tablename__ = 'user'
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre_id = Column(Integer(), ForeignKey('genre.id'))
    favorite_genre = relationship('favorite_genre', foreign_keys=favorite_genre_id)

