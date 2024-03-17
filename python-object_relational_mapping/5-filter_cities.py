#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state

Takes 4 arguments: username, password, database name
and state_name
No argument validation needed
Uses the module MySQLdb (import MySQLdb)
connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by cities.id
Code is not be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    _, username, password, db_name, state_name = sys.argv
    host = "localhost"
    port = 3306
    db = MySQLdb.connect(user=username, password=password,
                         host=host, port=port, database=db_name)
    with db.cursor() as cur:
        cur.execute(
            """SELECT A.name
            FROM cities AS A
            JOIN states AS B ON A.state_id = B.id
            WHERE BINARY B.name = %s
            ORDER BY A.id ASC;""",
            (state_name, )
        )

        print(* [name[0] for name in cur.fetchall()], sep=", ")

    db.close()
