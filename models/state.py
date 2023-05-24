#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state')
    else:
        name = ''

        @property
        def cities(self):
            from models import storage
            from models.city import City
            return [city for city in storage.all(City)
                    if city.state_id == self.id]
