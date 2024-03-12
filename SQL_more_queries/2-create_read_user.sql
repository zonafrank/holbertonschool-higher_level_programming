-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- creates the database hbtn_0d_2 if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
use hbtn_0d_2;
-- Create user user_0d_2 with password should be set to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
