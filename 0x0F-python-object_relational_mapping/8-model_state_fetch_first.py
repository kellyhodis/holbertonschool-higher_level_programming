#!/usr/bin/python3
""" This is a module containing a script that lists the first State object
from the hbtn_0e_6_usa database. """

from model_state import Base, State
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
    first_state = session.query(State).filter(State.id == 1).first()
    if not first_state:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
