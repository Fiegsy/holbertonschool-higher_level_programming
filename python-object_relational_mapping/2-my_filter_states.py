#!/usr/bin/python3
"""
Lists all states from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'\
                   ORDER BY states.id".format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()