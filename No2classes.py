#Class 1
class Book:
    def __init__(self, title, author_id, isbn, publication_date, genre_id, availability=True, book_id=None):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.genre_id = genre_id
        self.availability = availability
        self.book_id = book_id

    def save_db(self, connector):
        try:
            query = """
            INSERT INTO books (title, 
                               author_id, 
                               isbn, 
                               publication_date,
                               genre_id, 
                               availability)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            connector.cursor.execute(query, 
                                     (self.title, self.author_id, self.isbn, self.publication_date, self.genre_id, self.availability))
            connector.connection.commit()
            print("Title has been recorded into our data base!")
            print("A+ for success!")
        except Exception as e:
            print(f"Error message: {e}") 
    
#Class 2
class Author:
    def __init__(self, name, biography, author_id=None):
        self.name = name
        self.biography = biography
        self.author_id = author_id

    def save_db(self, connector):
        try:
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            connector.cursor.execute(query, 
                                     (self.name, self.library_id))
            connector.connection.commit()
            print("User added successfully!")
        finally:
            connector.close_connection()

#Class 3
class User:
    def __init__(self, name, library_id, user_id=None):
        self.name = name
        self.library_id = library_id
        self.user_id = user_id
    
    def save_db(self, connector):
        try:
            query = """
            INSERT INTO users (name, 
                               library_id)
            VALUES (%s, %s)
            """
            connector.cursor.execute(query, 
                                     (self.name, self.library_id))
            connector.connection.commit()
            print("New user has been added to database!")
        except Exception as e:
            print(f"Error message: {e}")

#class 4
class Genre:
    def __init__(self, genre_type=None, genre_id=None):
        self.genre_type = genre_type
        self.genre_id = genre_id

    def save_db(self, connector):
        try:
            if not self.genre_type:
                print("Genre type is required to save to the database.")
                return

            query = """
            INSERT INTO genres (genre_type)
            VALUES (%s)
            """
            connector.cursor.execute(query, 
                                     (self.genre_type,))
            connector.connection.commit()
            print("...processing")
            print(f"Genre '{self.genre_type}' documented successfully.")
        except Exception as e:
            print(f"Error while saving genre: {e}")

    def retrieve_genre(self, connector):
        try:
            query = "SELECT id, genre_type FROM genres"
            connector.cursor.execute(query)
            return connector.cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving genres: {e}")
            return []