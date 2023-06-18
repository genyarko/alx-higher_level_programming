#!/usr/bin/python3
"""
Lists states based on the given argument (safe from MySQL injections)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Lists all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injections)
    """
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the query with parameterized values
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
