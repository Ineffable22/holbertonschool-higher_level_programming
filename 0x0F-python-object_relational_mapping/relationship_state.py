#!/usr/bin/python3
"""
First state model
Definition of the State class
Models State inherits from base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Class definition of a State and an instance
    Base = declarative_base() """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state")
