#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Table, Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column('amenitiy_id', String(60),
                             ForeignKey("amenities.id"), nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", backref="place",
                           cascade="all,delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def amenities(self):
        amenitylist = []
        for am in models.storage.all(Amenity):
            if am.place_id == self.amenity_ids:
                amenitylist.append(am)
        return amenitylist

    @amenities.setter
    def amenities(self, obj):
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)

    @property
    def reviews(self):
        reviewlist = []
        for rev in models.storage.all(Review):
            if rev.place_id == self.id:
                reviewlist.append(rev)
        return reviewlist
