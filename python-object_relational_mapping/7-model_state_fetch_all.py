#!/usr/bin/python3
"""Links State class to table in database"""

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
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
