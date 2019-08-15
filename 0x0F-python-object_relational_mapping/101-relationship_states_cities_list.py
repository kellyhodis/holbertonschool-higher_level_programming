#!/usr/bin/python3
""" Lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa.
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]

    sql = "mysql+mysqldb://{}:{}@localhost/{}".format(mysql_username,
                                                      mysql_password,
                                                      mysql_database)
    engine = create_engine(sql, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    objects = session.query(State).join(State.cities).order_by(State.id).all()

    for state in objects:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
