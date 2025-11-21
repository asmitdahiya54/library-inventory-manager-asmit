import unittest
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

class TestLibraryManager(unittest.TestCase):

    def test_book_issue(self):
        book = Book("Python", "Guido", "111")
        self.assertTrue(book.issue())
        self.assertEqual(book.status, "issued")

    def test_book_return(self):
        book = Book("Python", "Guido", "111", status="issued")
        self.assertTrue(book.return_book())
        self.assertEqual(book.status, "available")

    def test_add_book(self):
        inventory = LibraryInventory(file_path="data/test_books.json")
        inventory.books = []  # reset for test

        result = inventory.add_book("AI", "Andrew Ng", "222")
        self.assertTrue(result)

    def test_search_by_title(self):
        inventory = LibraryInventory(file_path="data/test_books.json")
        inventory.books = [
            Book("Machine Learning", "Tom", "333"),
            Book("Deep Learning", "Ian", "444")
        ]

        results = inventory.search_by_title("Learning")
        self.assertEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()
