/*
CREATE DATABASE library_db;
*/
USE library_db;

/*TABLE CREATIONS*/
/*
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);


CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

SELECT *
FROM authors
INNER JOIN books
ON authors.id = books.author_id;

*/

/*
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
*/

/*
CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre_type VARCHAR(255) NOT NULL
);

ALTER TABLE books
ADD COLUMN genre_id INT,
ADD FOREIGN KEY (genre_id) REFERENCES genres(id);
*/


/*I DID NOT use this for this project unlike in the previous assignment. I keep it as like a backup*/
/* Based on exp, MYSQL becomes really annoying to connect. I used this for HW3 and it solved my issue!*/
/*
GRANT ALL PRIVILEGES ON gym_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
*/




SELECT * FROM books