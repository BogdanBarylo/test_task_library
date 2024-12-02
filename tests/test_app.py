import unittest
import os
from exception import BookNotFoundError
from library_model import Library
from validate import validate_title, validate_author, validate_year, validate_status


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_file = os.path.join("tests", "test_library.json")
        self.library = Library(file_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        self.library.add_book("Анна Каренина", "Лев Толстой", 1877)
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].title, "Война и мир")
        self.assertEqual(self.library.books[1].author, "Лев Толстой")

    def test_remove_nonexistent_book(self):
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book(99)

    def test_update_book_status_invalid_id(self):
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        with self.assertRaises(BookNotFoundError):
            self.library.update_book_status(99, "выдана")

    def test_search_books_multiple_criteria(self):
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        self.library.add_book("Анна Каренина", "Лев Толстой", 1877)
        results = self.library.search_books(author="Лев Толстой", year=1869)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Война и мир")

    def test_save_and_load_books(self):
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        self.library.save_books()

        new_library = Library(file_path=self.test_file)
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "Война и мир")


class TestValidation(unittest.TestCase):
    def test_validate_title(self):
        self.assertEqual(validate_title("Война и мир"), "Война и мир")
        with self.assertRaises(ValueError):
            validate_title("")
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_validate_author(self):
        self.assertEqual(validate_author("Лев Толстой"), "Лев Толстой")
        with self.assertRaises(ValueError):
            validate_author("")
        with self.assertRaises(ValueError):
            validate_author("   ")

    def test_validate_year(self):
        self.assertEqual(validate_year(2023), 2023)
        self.assertEqual(validate_year(1), 1)
        with self.assertRaises(ValueError):
            validate_year(0)
        with self.assertRaises(ValueError):
            validate_year(3000)
        with self.assertRaises(ValueError):
            validate_year(-10)

    def test_validate_status(self):
        self.assertEqual(validate_status("в наличии"), "в наличии")
        self.assertEqual(validate_status("выдана"), "выдана")
        with self.assertRaises(ValueError):
            validate_status("неизвестный статус")
        with self.assertRaises(ValueError):
            validate_status("")


if __name__ == "__main__":
    unittest.main()
