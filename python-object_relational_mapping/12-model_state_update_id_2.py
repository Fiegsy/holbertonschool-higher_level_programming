#!/usr/bin/python3
"""
This script updates the name of the State object with id=2 to "New Mexico"
in the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def update_state_name():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with id=2 not found.")

    session.close()

if __name__ == "__main__":
    update_state_name()
