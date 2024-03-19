#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a
from the database
Take arguments: mysql username, mysql password and database name
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

    states_with_a = session.query(State).filter(State.name.like("%a%")).all()

    for state in states_with_a:
        session.delete(state)

    session.commit()
    session.close()
