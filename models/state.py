#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('Cities', backref='state', cascade='delete')

    else:
        @property
        def cities(self):
            lista = []
            obje = storage.all(City)
            for key, value in obje.items():
                if value.state_id == self.id:
                    lista.append(value)
            return lista
