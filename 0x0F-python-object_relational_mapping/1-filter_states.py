#!/usr/bin/python3
"""This script lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=db,
            charset="utf8"
    )
    cur = conn.cursor()
    stmt = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(stmt)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
