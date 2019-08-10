#!/usr/bin/python3
""" This is a module containing a script that lists
all cities matching a specific state from the database hbtn_0e_4_usa."""

import sys
import MySQLdb


def list_all_match(mysql_username="", mysql_password="", database_name="",
                   match=""):
    ''' This is a function that lists all cities from a state
    from a database. '''
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    cur = conn.cursor()
    sql = "SELECT cities.name FROM cities"
    sql += " JOIN states ON state_id=states.id WHERE "
    sql += "states.name =%s ORDER BY cities.id ASC"
    cur.execute(sql, (match, ))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        if i != len(query_rows) - 1:
            print(query_rows[i][0], end=", ")
        else:
            print(query_rows[i][0])
    cur.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = sys.argv[4]
    list_all_match(username, password, database, match)
