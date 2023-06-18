#!/usr/bin/python3
"""
Lists states
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Lists all states from the database hbtn_0e_0_usa
    """
    # Database connection information
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the query to retrieve all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
