#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        cities = relationship(
                'City',
                cascade='all delete-orphan',
                backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            return [city for city in storage.all(City)
                    if city.state_id == self.id]
