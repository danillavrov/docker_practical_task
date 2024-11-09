import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


create_table_User = """
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""
create_table_Category = """
CREATE TABLE IF NOT EXISTS Category (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL
);
"""
create_table_Author = """
CREATE TABLE IF NOT EXISTS Author (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    second_name TEXT NOT NULL
);
"""
create_table_Book = """
CREATE TABLE IF NOT EXISTS Book (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    Author_id INTEGER,
    Category_id INTEGER,
    FOREIGN KEY (Author_id) REFERENCES Author(id),
    FOREIGN KEY (Category_id) REFERENCES Category(id)
);
"""
create_table_BookAuthor = """
CREATE TABLE IF NOT EXISTS BookAuthor (
    Book_id INTEGER PRIMARY KEY,
    Author_id INTEGER,
    Category_id INTEGER,
    FOREIGN KEY (Author_id) REFERENCES Author(id),
    FOREIGN KEY (Book_id) REFERENCES Book(id)
);
"""
create_table_BookOwner = """
CREATE TABLE IF NOT EXISTS BookOwner (
    User_id INTEGER PRIMARY KEY,
    Book_id INTEGER,
    FOREIGN KEY (User_id) REFERENCES User(id),
    FOREIGN KEY (Book_id) REFERENCES Book(id)
);
"""

cursor.execute(create_table_Category)
cursor.execute(create_table_Author)
cursor.execute(create_table_Book)
cursor.execute(create_table_BookAuthor)
cursor.execute(create_table_BookOwner)
cursor.execute(create_table_User)
connection.commit()


# СОЗДАНИЕ ЮЗЕРОВ
cursor.execute("INSERT INTO user (name, emai) VALUES (?, ?);", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO user (name, emai) VALUES (?, ?);", ("Bob", "bob@example.com"))
cursor.execute("INSERT INTO user (name, emai) VALUES (?, ?);", ("jack", "jack@example.com"))

# СОЗДАНИЕ КАТЕГОРИЙ
cursor.execute("INSERT INTO Category (category) VALUES (?);", ("Fantastic",))
cursor.execute("INSERT INTO Category (category) VALUES (?);", ("Science",))
cursor.execute("INSERT INTO Category (category) VALUES (?);", ("Non-Fiction",))

# СОЗДАНИЕ АВТОРОВ
cursor.execute("INSERT INTO Author (name, second_name) VALUES (?, ?);", ("leo", "tolstoy"))
cursor.execute("INSERT INTO Author (name, second_name) VALUES (?, ?);", ("brothers", "strugatskie"))
cursor.execute("INSERT INTO Author (name, second_name) VALUES (?, ?);", ("arkady", "perelman"))

# SOZDANIE KNIG
cursor.execute("INSERT INTO Book (name, Author_id, Category_id) VALUES (?, ?, ?);", ("war and peace", 1, 1))
cursor.execute("INSERT INTO Book (name, Author_id, Category_id) VALUES (?, ?, ?);", ("crime and punishment", 2, 2))
cursor.execute("INSERT INTO Book (name, Author_id, Category_id) VALUES (?, ?, ?);", ("interesting physics", 3, 3))

# SVAZ KNIG I AVTOROV
cursor.execute("INSERT INTO BookAuthor (Book_id, Author_id, Category_id) VALUES (?, ?, ?);", (1, 1, 1))
cursor.execute("INSERT INTO BookAuthor (Book_id, Author_id, Category_id) VALUES (?, ?, ?);", (2, 2, 2))
cursor.execute("INSERT INTO BookAuthor (Book_id, Author_id, Category_id) VALUES (?, ?, ?);", (3, 3, 3))

#             === USE CASE ===

# Alice take war and peace
cursor.execute("INSERT INTO BookOwner (Book_id, User_id) VALUES (?, ?);", (3, 1))

# Alice take back war and peace
cursor.execute("SELECT id FROM user WHERE name = ?;", ("Alice",))
user_id = cursor.fetchone()[0]
cursor.execute("DELETE FROM BookOwner WHERE User_id = ?;", (user_id,))

# Jack take crime and punishment
cursor.execute("INSERT INTO BookOwner (Book_id, User_id) VALUES (?, ?);", (2, 3))

# Jack loses crime and punishment
cursor.execute("DELETE FROM BookOwner WHERE Book_id = (SELECT id FROM Book WHERE name = ?);", ("crime and punishment",))
cursor.execute("DELETE FROM BookAuthor WHERE Book_id = (SELECT id FROM Book WHERE name = ?);", ("crime and punishment",))
cursor.execute("DELETE FROM Book WHERE name = ?;", ("crime and punishment",))

# search book by author ex. leo tolstoy
cursor.execute("SELECT id FROM Author WHERE name = ? AND second_name = ?;", ("leo", "tolstoy"))
author_id = cursor.fetchone()[0]
cursor.execute("SELECT book_id FROM BookAuthor WHERE author_id = ?;", (author_id,))
book_id = cursor.fetchone()[0]
cursor.execute("SELECT name FROM Book WHERE id = ?;", (book_id,))
print(cursor.fetchone()[0])

connection.commit()
connection.close()
