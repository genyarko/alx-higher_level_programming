-- Script: List All Records with Name and Score

-- Description: This script lists all records of the table second_table in the hbtn_0c_0 database, filtering out rows without a name value.

-- SQL query to list all records with name and score, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
