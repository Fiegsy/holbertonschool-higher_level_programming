#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def add_louisiana_state():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("New state added with id:", new_state.id)

    session.close()

if __name__ == "__main__":
    add_louisiana_state()
