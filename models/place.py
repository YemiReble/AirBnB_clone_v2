#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('citie.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=True)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete-orphan',
                backref='place')
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                back_populates='place_amenities',
                viewonly=False
                )
    else:
        @property
        def reviews(self):
            """Getter for all reviews with place_id attribut equal self.id"""
            from models.review import Review
            return [review
                    for review in storage.all(Review)
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute"""
            from models.amenity import Amenity
            self.amenity_ids = [
                    amenity
                    for amenity in storage.all(Amenity)
                    if amenity.place_id == self.id]
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute"""
            if type(obj) is not Amenity:
                return
            self.amenity_ids.append(obj)


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               nullable=False),
        Column('amenity_id', String(60), ForeignKey('ameities.id'),
               nullable=False))
