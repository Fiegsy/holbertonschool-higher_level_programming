#!/usr/bin/python3
"""Module that List all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3], charset="utf8")

    c = db.cursor()
    c.execute("""SELECT * FROM states
              ORDER BY states.id""")
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()