#!/usr/bin/python3
"""Links State class to table in database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    _, username, password, db = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
