#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ The amenity class """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
