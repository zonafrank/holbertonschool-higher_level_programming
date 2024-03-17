#!/usr/bin/python3
"""
a  script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument:

Takes 4 arguments: username, password, database name
and state name searched
No argument validation needed
Uses the module MySQLdb (import MySQLdb)
connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
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
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id",
        (state_name,)
    )

    for row in cur.fetchall():
        print(row)
    db.close()
