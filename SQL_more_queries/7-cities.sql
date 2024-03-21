-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    city_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city_name VARCHAR(256) NOT NULL,
    population INT NOT NULL,
    state VARCHAR(100) NOT NULL
);
