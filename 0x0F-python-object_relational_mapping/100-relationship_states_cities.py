#!/usr/bin/python3
""" Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
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

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
