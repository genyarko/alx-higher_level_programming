-- Script: Update Score of Bob

-- Description: This script updates the score of Bob to 10 in the table second_table of the hbtn_0c_0 database.

-- SQL query to update the score of Bob to 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
