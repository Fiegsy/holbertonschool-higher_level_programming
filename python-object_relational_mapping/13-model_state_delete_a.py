#!/usr/bin/python3
"""
Deletes all State objects with names containing the letter "a" from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
   
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}")

    
    Session = sessionmaker(bind=engine)
    session = Session()

    
    session.query(State).filter(State.name.contains("a")).delete()
    session.commit()

    
    session.close()
