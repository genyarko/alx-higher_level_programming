#!/usr/bin/python3
"""
Lists cities of a specific state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Lists all cities of a specific state using the hbtn_0e_4_usa database
    """
    # Database connection information
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Prepare the query with placeholders and execute it with parameters
    query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
