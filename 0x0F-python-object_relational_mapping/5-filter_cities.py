#!/usr/bin/python3
""" This script lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


def connection(username, passwd, database):
    """ ingresamos variables con argumentos """
    try:
        return MySQLdb.connect(host='localhost',
                               port=3306,
                               user=username,
                               passwd=passwd,
                               db=database)
    except Exception:
        print("Can't connect to database")


if __name__ == '__main__':
    db = connection(argv[1], argv[2], argv[3])
    cur = db.cursor()
    try:
        cur.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON
        states.id=cities.state_id
        AND states.name=%s;
        """, (argv[4], )
        )
        stores = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s".format(e.sys.argv[0], e.sys.argv[1]))
        except IndexError:
            print("MySql Error: %s".format(str(e)))
    print(*[i[0] for i in stores], sep=", ")
    cur.close()
    db.close()
