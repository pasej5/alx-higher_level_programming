#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The primary key for the state record.
        name (str): The name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
