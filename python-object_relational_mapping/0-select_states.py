#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    databse =  MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        databse=argv[3])
    cursor = databse.cursor()
    cursor.execute("SELECT * FROM states")
    for i in cursor:
        print(i)
    cursor.close()
    databse.close()