#!/usr/bin/python3
""" This script lists all State objects with the name passed as argument
from database hbtn_0e_6_usa """
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State)
        state = state.filter_by(name=argv[4]).first()
        print("{}".format(state.id))
    except Exception:
        print("Not found")
    session.close()
