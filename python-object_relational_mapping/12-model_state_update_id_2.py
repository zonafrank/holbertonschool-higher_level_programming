#!/usr/bin/python3
"""
script that changes the name of a State object from the database
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

    state = session.query(State).filter_by(id=2).first()
    if state is None:
        print("state with id 2 not found")
    else:
        state.name = "New Mexico"
        session.commit()

    session.close()
