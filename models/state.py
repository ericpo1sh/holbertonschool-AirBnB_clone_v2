#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="state")
    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """returns list of City instances upon state_id"""
            cities_list = []
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_list
