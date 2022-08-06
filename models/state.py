#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # creating relationship with cities
    storage_type = os.getenv("HBNB_TYPE_STORAGE")
    if storage_type == "db":
        cities = relationship("City",
                              cascade="all, delete",
                              backref="state")
    else:
        @property
        def cities(self):
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
