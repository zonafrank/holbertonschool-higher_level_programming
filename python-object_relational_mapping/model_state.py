#!/usr/bin/python3

"""
 Module contains the class definition of a State which inherits
 from an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string
    with maximum 128 characters and can’t be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definitionfor State model"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
