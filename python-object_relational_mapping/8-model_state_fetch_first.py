#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("No states found")

    session.close()
