#!/usr/bin/python3
""" This script lists all City objects from the database hbtn_0e_101_usa """
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
    table = session.query(City)
    table = table.order_by(City.id).all()
    for city in table:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
