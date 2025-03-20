import mysql.connector

class db_connector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bebop1216!",
            database="library_db"
        )
        self.cursor = self.connection.cursor()

    def query_execution(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_data(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close() 
        self.connection.close()