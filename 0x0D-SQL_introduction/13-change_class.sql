-- Script: Remove Records with Score <= 5

-- Description: This script removes all records with a score less than or equal to 5 from the table second_table of the hbtn_0c_0 database.

-- SQL query to remove records with score <= 5 from the second_table
DELETE FROM second_table
WHERE score <= 5;
