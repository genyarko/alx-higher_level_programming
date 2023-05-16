-- Script: List Records Count by Score

-- Description: This script lists the number of records with the same score in the table second_table of the hbtn_0c_0 database.

-- SQL query to list the number of records with the same score, sorted by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
