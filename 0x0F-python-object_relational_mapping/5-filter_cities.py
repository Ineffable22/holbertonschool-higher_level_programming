#!/usr/bin/python3
""" This script lists all cities from the database hbtn_0e_4_usa """
if __name__ == '__main__':
    import MySQLdb
    import sys
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    except Exception:
        print("Can't connect to database")
    cur = db.cursor()
    try:
        cur.execute(
            """
            SELECT cities.name
            FROM cities
            WHERE state_id=
            (SELECT states.id FROM states WHERE name =%s)
            ORDER BY cities.id
            """, (sys.argv[4], )
        )
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s".format(e.sys.argv[0], e.sys.argv[1]))
        except IndexError:
            print("MySql Error: %s".format(str(e)))
    flag = 0
    total = ""
    for row in rows:
        if flag == 1:
            total += ", "
        flag = 1
        total += row[0]
    print(total)
    cur.close()
    db.close()
