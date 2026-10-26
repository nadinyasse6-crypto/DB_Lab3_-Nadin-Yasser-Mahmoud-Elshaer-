CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Drop table if exists to ensure clean schema rebuild
DROP TABLE IF EXISTS users;

-- 1. Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- 2. Author Table
CREATE TABLE IF NOT EXISTS author (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

-- 3. Book Table (with ON DELETE CASCADE)
CREATE TABLE IF NOT EXISTS book (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES author(author_id) ON DELETE CASCADE
);