#!/usr/bin/python3
""" This script lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa """
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    table = session.query(State)
    table = table.order_by(State.id).all()
    for states in table:
        print("{}: {}".format(states.id, states.name))
        for city in states.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
