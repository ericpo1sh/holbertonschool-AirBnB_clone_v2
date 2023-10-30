#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity_table = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False
        )
    )


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            overlaps="place_amenities"
        )
        reviews = relationship(
            "Review",
            cascade="all, delete",
            backref="place"
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns list of Review instances upon place_id"""
            reviews_list = []
            for obj in list(models.storage.all(Review).values()):
                if obj.place_id == self.id:
                    reviews_list.append(obj)
            return reviews_list

        @property
        def amenities(self):
            """returns list of Amenity instances upon place_id"""
            amenities_list = []
            for obj in list(models.storage.all(Amenity).values()):
                if obj.place_id == self.id:
                    amenities_list.append(obj)
            return amenities_list

        @amenities.setter
        def amenities(self, obj=None):
            """setter for amenity_ids list - class attribute"""
            if obj:
                if type(obj) is Amenity and obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
