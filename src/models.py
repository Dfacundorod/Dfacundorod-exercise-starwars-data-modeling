import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    climate= Column(String, nullable=False)
    population= Column(Integer, nullable=False)
    terrain=Column(String, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    gender= Column(String, nullable=False)
    hair_color= Column(String, nullable=False)
    eye_color=Column(String, nullable=False)
    age=Column(Integer, nullable=False)
    planet=Column(Integer, ForeignKey('planets.planets_id'), nullable=False)

    planet = relationship(Planets)



class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    favorite_planet_id = Column(Integer, ForeignKey('planets.planet_id'), nullable=False)
    favorite_character_id = Column(Integer, ForeignKey('characters.character_id'), nullable=False)
    planets = relationship(Planets)
    characters = relationship(Characters)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
