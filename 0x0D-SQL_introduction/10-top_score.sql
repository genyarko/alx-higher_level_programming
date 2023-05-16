-- Script: List Records of second_table

-- Description: This script lists all records of the table second_table in the hbtn_0c_0 database.

-- SQL query to list all records of the second_table, ordered by score (top first)
SELECT score, name
FROM second_table
ORDER BY score DESC;
