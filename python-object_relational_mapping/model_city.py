#!/usr/bin/python3
"""Lists that have the definition of the City class"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines the City class which is linked to the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id', ondelete="CASCADE"))