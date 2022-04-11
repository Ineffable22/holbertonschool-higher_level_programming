#!/usr/bin/python3
""" This script creates the State “California” with the City
San Francisco from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py) """
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()
    session.close()
