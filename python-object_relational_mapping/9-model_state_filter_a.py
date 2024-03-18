#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a
Take 3 arguments: mysql username, mysql password and database name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    _, username, password, db = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db),
        pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    result = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))

    session.close()
