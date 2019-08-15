#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates="State")

    @property
    def cities(self):
        seto = []
        tocheck = models.storage.all(City)
        for values in tocheck.values():
            if values.state_id == self.state_id:
                seto.append(values)
        return(seto)
