#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

#!/usr/bin/python3
"""List all states"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
   database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],database=sys.argv[3])
    cur =database.cursor()
    cur.execute("SELECT * FROM states")
    for i in cur.fetchall():
        print(i)

    cur.close()
   database.close()