
def add_new_book(connector):
    try:
        title = input("Title: ")
        author_id = int(input("Author ID: "))

        author_query = "SELECT * FROM authors WHERE id = %s"
        connector.cursor.execute(author_query, (author_id,))
        author = connector.cursor.fetchone()

        if author is None:
            print(f"Author ID {author_id} does not exist. Please add an author to the database first.")
            return

        isbn = input("ISBN: ")
        publication_date = input("Type date (YYYY-MM-DD): ")

        genre = Genre()
        genres = genre.retrieve_genre(connector)
        if not genres:
            print("No genres available in the database.")
            return

        print("\nCurrent genres:")
        for x in genres:
            print(f"{x[0]}: {x[1]}")

        genre_id = input("Enter the genre ID (or 'n' to add a new genre): ")
        if genre_id.lower() == 'n':
            new_genre_type = input("Enter the new genre type: ")
            new_genre = Genre(genre_type=new_genre_type)
            new_genre.save_db(connector)
            genres = new_genre.retrieve_genre(connector)
            genre_id = genres[-1][0]
        else:
            genre_id = int(genre_id)

        book = Book(
            title=title,
            author_id=author_id,
            isbn=isbn,
            publication_date=publication_date,
            genre_id=genre_id
        )
        book.save_db(connector)
        print("Newly added title has successfully uploaded into database!")

    except Exception as e:
        print(f"Error: {e}")


def return_book(connector):
    try:
        user_id = int(input("Type user ID: "))
        query = """
        SELECT bb.id, b.title, b.id AS book_id
        FROM borrowed_books AS bb
        INNER JOIN books AS b ON bb.book_id = b.id
        WHERE bb.user_id = %s AND bb.return_date IS NULL
        """
        connector.cursor.execute(query, 
                                 (user_id,))
        borrowed_books = connector.cursor.fetchall()

        if not borrowed_books:
            print(f"No borrowed book on record {user_id}.")
            return

        #which books have been borrowed
        print("Borrowed Books:")
        for x in borrowed_books:
            print(f"Transaction ID: {x[0]}, Book Title: {x[1]}")

        #book to return
        transaction_id = int(input("ID of the book to return: "))
        return_date = input("Type date & apply proper format (YYYY-MM-DD): ")

        #book to borrow
        update_borrowed = "UPDATE borrowed_books SET return_date = %s WHERE id = %s"
        update_book = "UPDATE books SET availability = 1 WHERE id = %s"
        connector.cursor.execute(update_borrowed, 
                                 (return_date, transaction_id))
        connector.cursor.execute(update_book, (borrowed_books[0][2],))
        connector.connection.commit()

        print(f"Book '{borrowed_books[0][1]}' has been returned by User ID {user_id}.")

    except Exception as e:
        print(f"Error during the return process: {e}")

def search_book(connector):
    try:
        print("Searching...:")
        title = input("Enter title: ")
        print("loading...:")

        query = """
        SELECT b.id, b.title
        FROM books AS b
        WHERE b.title LIKE %s
        """
        connector.cursor.execute(query, 
                                 (f"%{title}%",))

        books = connector.cursor.fetchall()
        if not books:
            print("Title not found in database.")
            print("...please try again")
        else:
            print("Based on the results...:")
            for book in books:
                print(f"ID: {book[0]} | Title: {book[1]}")

    except Exception as e:
        print(f"Error: {e}")

def display_books(connector):
    try:
        query = "SELECT b.id, b.title, a.name, b.isbn, b.publication_date, b.availability " \
                "FROM books AS b INNER JOIN authors AS a ON b.author_id = a.id"
        connector.cursor.execute(query)
        books = connector.cursor.fetchall()

        if not books:
            print("No books available in the library.")
        else:
            print("Our complete catalog....")
            for book in books:
                availability = "Available" if book[5] else "Borrowed"
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, "
                      f"Publication Date: {book[4]}, Status: {availability}")

    except Exception as e:
        print(f"Error displaying books: {e}")

#FUNCTIONS FOR CLASS#3----------

def add_new_user(connector):
    try:
        name = input("Enter the user's first and last name: ")
        library_id = input("library ID: ")

        query = """
        INSERT INTO users (name, library_id)
        VALUES (%s, %s)
        """
        connector.cursor.execute(query, 
                                 (name, library_id))
        connector.connection.commit()

        print(f"User '{name}' has been registered!")
    except Exception as e:
        print(f"Error: {e}")

def borrow_book(connector):
    try:
        user_id = int(input("Enter the user ID: "))
        user_query = "SELECT * FROM users WHERE id = %s"
        connector.cursor.execute(user_query, (user_id,))
        user = connector.cursor.fetchone()
        if not user:
            print(f"No user found with ID {user_id}. Please try again.")
            return
        
        book_id = int(input("Enter the book ID to borrow: "))
        book_query = "SELECT * FROM books WHERE id = %s AND availability = 1"
        connector.cursor.execute(book_query, (book_id,))
        book = connector.cursor.fetchone()
        if not book:
            print(f"Book ID {book_id} is either unavailable or does not exist.")
            return

        borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
        borrow_query = """
        INSERT INTO borrowed_books (user_id, 
                                    book_id, 
                                    borrow_date)
        VALUES (%s, %s, %s)
        """
        connector.cursor.execute(borrow_query, 
                                 (user_id, book_id, borrow_date))
        connector.connection.commit()
        print(f"Book ID {book_id} has been successfully borrowed by User ID {user_id}.")

        update_query = "UPDATE books SET availability = 0 WHERE id = %s"
        connector.cursor.execute(update_query, 
                                 (book_id,))
        connector.connection.commit()

    except Exception as e:
        print(f"Error during borrowing process: {e}")

def view_user_details(connector):
    try:
        print("Search by user name:")
        name = input("Enter the user's name: ")
        query = """
        SELECT id, name
        FROM users
        WHERE name LIKE %s
        """
        connector.cursor.execute(query, 
                                 (f"%{name}%",))

        users = connector.cursor.fetchall()
        if not users:
            print("Registered user does not exist\n...retry again!")
        else:
            print("Based on the results...:")
            for user in users:
                print(f"ID: {user[0]} | Name: {user[1]}")

    except Exception as e:
        print(f"Error: {e}")

def display_users(connector):
    try:
        query = "SELECT id, name, library_id FROM users"
        connector.cursor.execute(query)
        users = connector.cursor.fetchall()

        if not users:
            print("No user in databse")
        else:
            print("...searched users within the current system:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")

    except Exception as e:
        print(f"Error displaying users: {e}")

#FUNCTIONS FOR CLASS#2----------

def add_new_author(connector):
    try:
        name = input("Enter the author's name: ")
        biography = input("Enter the author's biography: ")

        query = """
        INSERT INTO authors (name, biography)
        VALUES (%s, %s)
        """
        connector.cursor.execute(query, 
                                 (name, biography))
        connector.connection.commit()

        print(f"Author '{name}' has been registered!")
    except Exception as e:
        print(f"Error: {e}")


def view_author_details(connector):
    try:
        print("Search by author name:")
        name = input("Enter the author's name: ")

        query = """
        SELECT id, name, biography
        FROM authors
        WHERE name LIKE %s
        """
        connector.cursor.execute(query, 
                                 (f"%{name}%",))

        authors = connector.cursor.fetchall()
        if not authors:
            print("Registered author does not exist\n...retry again!")
        else:
            print("Based on the results...:")
            for author in authors:
                print(f"ID: {author[0]} | Name: {author[1]} | Biography: {author[2]}")
    except Exception as e:
        print(f"Error: {e}")

def display_authors(connector):
    try:
        query = "SELECT id, name, biography FROM authors"
        connector.cursor.execute(query)
        authors = connector.cursor.fetchall()

        if not authors:
            print("No authors within this current system...")
        else:
            print("...current authors within the data base:")
            for author in authors:
                print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
    except Exception as e:
        print(f"Error: {e}")