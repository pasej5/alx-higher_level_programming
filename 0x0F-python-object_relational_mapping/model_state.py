#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base class for your SQLAlchemy models
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

