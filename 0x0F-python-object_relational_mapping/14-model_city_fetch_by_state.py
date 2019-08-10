#!/usr/bin/python3
""" This is a module containing a script that prints all City objects
from the hbtn_0e_14_usa database. """

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sql = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password,
                                                      database)
    engine = create_engine(sql, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    cities = session.query(City).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state_id, city.id, city.name))
