#!/usr/bin/python3
""" This is a module to define the State class. """

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    ''' Definition of State class, inheriting from Base
    in declarative_base of SQLAlchemy. '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
sql = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                  password,
                                                  database)

engine = create_engine(sql, pool_pre_ping=True)

Session = sessionmaker()
Session.configure(bind=engine)

Base.metadata.create_all(engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
