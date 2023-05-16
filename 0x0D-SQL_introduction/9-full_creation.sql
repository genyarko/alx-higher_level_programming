-- Script: Create second_table and Add Multiple Rows

-- Description: This script creates the table second_table in the hbtn_0c_0 database and adds multiple rows to it.

-- SQL query to create the second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- SQL query to add multiple rows to the second_table
INSERT INTO second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

