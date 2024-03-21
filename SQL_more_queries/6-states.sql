-- Create the database my_database if it doesn't exist
CREATE DATABASE IF NOT EXISTS my_database;

-- Use the my_database database
USE my_database;

-- Create the countries table if it doesn't exist
CREATE TABLE IF NOT EXISTS countries (
    country_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(256) NOT NULL
);
