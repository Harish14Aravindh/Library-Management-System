from abc import ABC, abstractmethod


# Parent class for abstraction
class Base(ABC):

    @abstractmethod
    def display_info(self):
        pass


# Class Book
class Book(Base):

    def __init__(self, title, author):
        self.__title = title       # Encapsulation
        self.__author = author
        self.__available = True

    # Getter methods
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def available(self):
        return self.__available

    # Update availability
    def set_availability(self, status):
        self.__available = status

    # Polymorphism
    def display_info(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"{self.__title} by {self.__author} [{status}]")

    # String representation
    def __str__(self):
        status = "Available" if self.__available else "Borrowed"
        return f"{self.__title} by {self.__author} [{status}]"


# Class Library
class Library(Base):

    def __init__(self):
        self.__books = []          # Encapsulation

    def add_book(self, book):
        self.__books.append(book)

    def borrow(self, title):
        for book in self.__books:
            if book.title == title:

                if book.available:
                    book.set_availability(False)
                    print(f"'{title}' borrowed successfully.")
                else:
                    print(f"Sorry, '{title}' is already borrowed.")

                return

        print(f"No book titled '{title}'.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:

                if not book.available:
                    book.set_availability(True)
                    print(f"'{title}' returned successfully.")
                else:
                    print(f"'{title}' was not borrowed.")

                return

        print(f"No book titled '{title}'.")

    def show_books(self):
        print("\nLibrary Books:")
        for book in self.__books:
            print(book)

    # Polymorphism
    def display_info(self):
        print(f"Library contains {len(self.__books)} books.")


# Polymorphism demonstration
def show_details(obj):
    obj.display_info()


# Main program
book1 = Book("Python 101", "Rao")
book2 = Book("Java Basics", "James")
book3 = Book("C Programming", "Dennis")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

print("\n--- Borrow Book ---")
library.borrow("Python 101")
library.borrow("Python 101")

library.show_books()

print("\n--- Return Book ---")
library.return_book("Python 101")

library.show_books()

print("\n--- OOP Demonstration ---")
show_details(book1)
show_details(library)
