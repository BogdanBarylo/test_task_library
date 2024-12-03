from typing import Optional, List
from app.exception import BookNotFoundError
from app.model import Book
import os
import json


class Library:
    def __init__(self, file_path: str = "library.json"):
        self.file_path = file_path
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book(**item) for item in data]
        return []

    def save_books(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in self.books],
                      file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Book:
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        return new_book

    def remove_book(self, book_id: int) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
        else:
            raise BookNotFoundError(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)

    def search_books(self, **kwargs) -> List[Book]:
        result = self.books
        for key, value in kwargs.items():
            if value:
                result = [book for book in result if str(
                    getattr(book, key)).lower() == str(value).lower()]
        return result

    def update_book_status(self, book_id: int, status: str) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
        else:
            raise BookNotFoundError(f"Книга с ID {book_id} не найдена.")
