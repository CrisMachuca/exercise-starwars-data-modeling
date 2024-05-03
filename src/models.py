import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    register_date = Column(String(250), nullable=False)
    id_favorite_character = Column(String(250), nullable=False)
    id_favorite_planet = Column(String(250), nullable=False)
    id_favorite_starship = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class FavCharacter(Base):
    __tablename__ = 'fav_character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_character = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
        
    

class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    nave_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)

class FavStarship(Base):
    __tablename__ = 'fav_starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_starship = Column(Integer, ForeignKey('starship.id'))
    starship = relationship(Starship)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)  

class FavPlanet(Base):
    __tablename__ = 'fav_planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
