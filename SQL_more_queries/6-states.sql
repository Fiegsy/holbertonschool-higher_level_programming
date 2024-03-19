-- Ensure that the database hbtn_0d_usa exists, or create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create a table named 'states' if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    state_id INT PRIMARY KEY AUTO_INCREMENT,
    state_name VARCHAR(255) NOT NULL
);
