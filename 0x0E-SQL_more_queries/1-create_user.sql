-- This script creates the MySQL server user user_0d_1.
-- Create a user if it doesn't exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant privileges
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
