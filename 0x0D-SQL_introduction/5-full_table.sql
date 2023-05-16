-- Script: Print Table Description

-- Description: This script prints the full description of the table first_table from the hbtn_0c_0 database in the MySQL server.

-- SQL query to retrieve the table description
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_KEY, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
