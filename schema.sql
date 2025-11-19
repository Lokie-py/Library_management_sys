-- Create Database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- Table: books
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year INT,
    availability INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: users
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: issued_books
CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    status ENUM('issued', 'returned') DEFAULT 'issued',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);

-- Insert Sample Books
INSERT INTO books (title, author, genre, year, availability) VALUES
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 3),
('1984', 'George Orwell', 'Dystopian', 1949, 2),
('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 4),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 2),
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Fantasy', 1997, 5),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 3),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 2),
('Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 3),
('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 1954, 4),
('Animal Farm', 'George Orwell', 'Political Fiction', 1945, 3);

-- Insert Sample Users
INSERT INTO users (name, email, password) VALUES
('John Doe', 'john.doe@email.com', 'password123'),
('Jane Smith', 'jane.smith@email.com', 'password123'),
('Mike Johnson', 'mike.johnson@email.com', 'password123'),
('Sarah Williams', 'sarah.williams@email.com', 'password123'),
('David Brown', 'david.brown@email.com', 'password123');

-- Insert Sample Issued Books
INSERT INTO issued_books (user_id, book_id, issue_date, status) VALUES
(1, 1, '2025-09-15', 'issued'),
(2, 5, '2025-09-20', 'issued'),
(3, 3, '2025-09-10', 'returned');

-- Update book availability after issuing
UPDATE books SET availability = availability - 1 WHERE book_id IN (1, 5);