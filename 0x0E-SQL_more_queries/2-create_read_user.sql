-- This script creates the database hbtn_0d_2 and the user user_0d_2.
-- Create a Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a User
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant privilege
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost';
