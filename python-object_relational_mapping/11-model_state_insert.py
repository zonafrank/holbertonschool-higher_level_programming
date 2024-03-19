#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database
passed as argument
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
    state_name = "Louisiana"
    louisiana = State(name=state_name)
    session.add(louisiana)
    session.commit()

    result = session.query(State).filter(
        State.name == state_name).first()

    print(result.id)
    session.close()
