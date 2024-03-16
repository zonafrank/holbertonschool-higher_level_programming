#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa:

Takes 3 arguments: username, password and database name
No argument validation needed
Uses the module MySQLdb (import MySQLdb)
connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
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
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    for row in cur.fetchall():
        print(row)
    db.close()
