#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
if storage_type == 'db':
    from models.place import PlaceAmenity


class Amenity(BaseModel, Base):
    """Amenity class"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary=PlaceAmenity,
            back_populates='amenities')
    else:
        name = ''
        place_id = ''
