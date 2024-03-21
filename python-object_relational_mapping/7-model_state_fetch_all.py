#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa using SQLAlchemy"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    
    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}')
    
    
    Base.metadata.create_all(engine)

    
    Session = sessionmaker(bind=engine)
    session = Session()

    
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    
    session.close()
