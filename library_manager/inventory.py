import json
import os
import logging
from library_manager.book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, file_path="data/books.json"):
        self.file_path = file_path
        self.books = []
        self.load_from_file()

    # ---------------------- LOAD DATA ----------------------
    def load_from_file(self):
        try:
            if not os.path.exists(self.file_path):
                self.books = []
                return

            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.books = [Book(**book) for book in data]

        except Exception as e:
            logging.error("Error loading file: %s", e)
            self.books = []

    # ---------------------- SAVE ---------------------------
    def save_to_file(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
        except Exception as e:
            logging.error("Error saving file: %s", e)

    # ---------------------- ADD BOOK ------------------------
    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("ISBN already exists!")
                return False
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_to_file()
        return True

    # ---------------------- SEARCH -------------------------
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books
