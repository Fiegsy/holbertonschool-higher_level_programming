#!/usr/bin/python3
"""
That lists all State objects from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()