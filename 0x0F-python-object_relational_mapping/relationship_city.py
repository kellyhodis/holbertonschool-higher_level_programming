#!/usr/bin/python3
""" This is a module to define the City class. """

from sqlalchemy import Column, Integer, String
from relationship_state import Base, State
from sqlalchemy import ForeignKey


class City(Base):
    ''' Definition of City class, inheriting from Base
    in Base of model_state. '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
