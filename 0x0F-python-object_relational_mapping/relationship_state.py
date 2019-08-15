#!/usr/bin/python3
""" This is a module to define the State class. """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    ''' Definition of State class, inheriting from Base
    in declarative_base of SQLAlchemy. '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
