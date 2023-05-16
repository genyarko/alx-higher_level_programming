# Script: List Tables in a Database
# Description: This script lists all the tables of a specified database in the MySQL server.

# Check if the database name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide the database name as an argument."
    exit 1
fi

# Retrieve the database name from the argument
database=$1

# SQL query to retrieve all tables in the specified database
query="SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '$database';"

# Execute the SQL query using the MySQL command line tool
mysql -u username -p'password' -h hostname -P port -e "$query"
