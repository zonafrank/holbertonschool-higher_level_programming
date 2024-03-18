#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database also passed as argument
Take 4 arguments: mysql username, mysql password, database name
and state_name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    _, username, password, db, state_name = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db),
        pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    result = session.query(State).filter(
        State.name == state_name).first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Not found")

    session.close()
