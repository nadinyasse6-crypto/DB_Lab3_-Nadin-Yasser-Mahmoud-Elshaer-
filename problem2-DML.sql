USE library;

-- Insert Seed Data for Authors
INSERT IGNORE INTO author (author_id, name, country) VALUES 
(1, 'Naguib Mahfouz', 'Egypt'),
(2, 'Taha Hussein', 'Egypt'),
(3, 'Ahmed Khaled Tawfik', 'Egypt');

-- Insert Seed Data for Books
INSERT IGNORE INTO book (book_id, title, price, author_id) VALUES 
(1, 'Palace Walk', 120.00, 1),
(2, 'Sugar Street', 130.00, 1),
(3, 'The Days', 95.00, 2),
(4, 'Utopia', 85.00, 3),
(5, 'Passages', 90.00, 3),
(6, 'Brain Drain', 100.00, 3);