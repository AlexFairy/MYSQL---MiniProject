

#Study notes for later!
#Within the code.

#-----------------------------IMPORTING FUNCTIONS-----------------------------------------------------------

import No2functions

#-----------------------------IMPORTING CLASS FILE----------------------------------------------------------
#this is for importing my classes, because I want the project to be organized!

import importlib
classes = importlib.import_module("No2classes")

Book = classes.Book
Author = classes.Author
User = classes.User
Genre = classes.Genre


#-----------------------------CONNECTOR--------------------------------------------------------------------

#I'm doing it this way, because I have several files in this folder that use mysql connector
#I don't want interference or issues when connecting
#Steps: (pre moves) import importlib.util (1) must specify file name (2) load module (3) access class (4) apply [establish + close]

#pre-move
import importlib.util

#(1)
module_name = "2.MySQLconnector"
module_path = "C:/Users/AlexM/CodingTemple/1. MYSQLPython HW.Proj/2. MySQLconnector.py"

#(2)
spec = importlib.util.spec_from_file_location(module_name, module_path)
mysql_connector_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mysql_connector_module)

#(3)
#Note: db_connector is a class in file "2. MySQLconnector.py"
db_connector = mysql_connector_module.db_connector

#(4) apply!
#remember to establish + close!
#call the class () to establish
connector = db_connector()
print("db has established connection! :)")
connector.close_connection() #this is from ./2.MySQLconnector.py


def main_user_input(connector):
    print("Welcome to the Wolves & Greyson Library Management System Co.!")
    print("We are located in Albuquerque, New Mexico.")
    
    while True:
        print("\nPlease view our selections below:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        user_input = input("Enter a selection:\n")
        
        if user_input == "1":
            while True:
                print("\nBook Operations:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Back to Main Menu")
                book_input = input("Enter a selection:\n")
                
                if book_input == "1":
                    No2functions.add_new_book(connector)
                elif book_input == "2":
                    No2functions.borrow_book(connector)
                elif book_input == "3":
                    No2functions.return_book(connector)
                elif book_input == "4":
                    No2functions.search_book(connector)
                elif book_input == "5":
                    No2functions.display_books(connector)
                elif book_input == "6":
                    break
                else:
                    print("Invalid selection, please try again.")
        
        elif user_input == "2":
            while True:
                print("\nUser Operations:")
                print("1. Add a new user")
                print("2. View user details")
                print("3. Display all users")
                print("4. Back to Main Menu")
                user_input = input("Enter a selection:\n")
                
                if user_input == "1":
                    No2functions.add_new_user(connector)
                elif user_input == "2":
                    No2functions.view_user_details(connector)
                elif user_input == "3":
                    No2functions.display_users(connector)
                elif user_input == "4":
                    break
                else:
                    print("Invalid selection, please try again.")
        
        elif user_input == "3":
            while True:
                print("\nAuthor Operations:")
                print("1. Add a new author")
                print("2. View author details")
                print("3. Display all authors")
                print("4. Back to Main Menu")
                author_input = input("Enter a selection:\n")
                
                if author_input == "1":
                    No2functions.add_new_author(connector)
                elif author_input == "2":
                    No2functions.view_author_details(connector)
                elif author_input == "3":
                    No2functions.display_authors(connector)
                elif author_input == "4":
                    break
                else:
                    print("Invalid selection, please try again.")
        
        elif user_input == "4":
            print("Thank you for using the Wolves & Greyson Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid entry! Try again.")

if __name__ == "__main__":
    try:
        connector = db_connector()  
        main_user_input(connector)
        
    finally:
        connector.close_connection()