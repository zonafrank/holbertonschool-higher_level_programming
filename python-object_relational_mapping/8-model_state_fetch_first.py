#!/usr/bin/python3
"""
Script that lists the first State object from the database

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
    result = session.query(State).order_by(State.id).first()

    if result is None:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))

    session.close()
