#!/usr/bin/python3
"""
a script lists all cities from the database hbtn_0e_4_usa:

Takes 3 arguments: username, password and database name
No argument validation needed
Uses the module MySQLdb (import MySQLdb)
connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by cities.id
Code is not be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    _, username, password, db_name = sys.argv
    host = "localhost"
    port = 3306
    db = MySQLdb.connect(user=username, password=password,
                         host=host, port=port, database=db_name)
    with db.cursor() as cur:
        cur.execute(
            """SELECT *
            FROM cities AS A
            JOIN states AS B ON A.state_id = B.id
            ORDER BY A.id ASC;"""
        )

        for row in cur.fetchall():
            print(row)

    db.close()
