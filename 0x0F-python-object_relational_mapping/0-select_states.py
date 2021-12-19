#!/usr/bin/python3
""" Listing states in database"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db_connection = MySQLdb.connect(user, passwd, db)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    result_row = cursor.fetchall()
    for row in result_row:
        print(row)
    cursor.close()
    db_connection.close()
