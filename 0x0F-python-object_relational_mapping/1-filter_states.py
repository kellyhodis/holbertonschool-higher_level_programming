#!/usr/bin/python3
""" This is a script that lists all states with a name starting with N
from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=database,
                       charset="utf8")
cur = conn.cursor()
sql = "SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC"
cur.execute(sql)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
