-- Script: List Databases
-- Description: This script lists all databases on the MySQL server.

-- Connect to the MySQL server
-- Replace 'username' and 'password' with your MySQL credentials
-- Replace 'hostname' with the actual hostname or IP address of your MySQL server
-- Replace 'port' with the port number used by your MySQL server (default is 3306)
mysql -u username -p'password' -h hostname -P port -e "
-- SQL query to retrieve all databases
SELECT DISTINCT TABLE_SCHEMA AS DatabaseName
FROM INFORMATION_SCHEMA.TABLES;
"
