#!/usr/bin/python3
"""script that prints all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    _, username, password, db = sys.argv

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db}",
        pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
