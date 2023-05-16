-- Script: List Records with Score >= 10

-- Description: This script lists all records with a score greater than or equal to 10 in the table second_table of the hbtn_0c_0 database.

-- SQL query to list records with score >= 10 from the second_table, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
