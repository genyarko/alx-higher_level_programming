#!/usr/bin/python3
"""
Displays states based on the given argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Displays all values in the states table of hbtn_0e_0_usa where name matches the argument
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

    # Execute the query to retrieve states based on the given argument
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
