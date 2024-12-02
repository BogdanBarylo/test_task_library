from typing import Optional
from model import Book
import os
import json


class Library:
    def __init__(self, file_path: str = "library.json"):
        self.file_path = file_path
        self.books: list[Book] = self.load_books()

    def load_books(self) -> list[Book]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book(**item) for item in data]
        return []

    def save_books(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in self.books], file,
                      ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {new_id}.")

    def remove_book(self, book_id: int) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)

    def search_books(self, **kwargs) -> list[Book]:
        result = self.books
        for key, value in kwargs.items():
            if value:
                result = [book for book in result if str(
                    getattr(book, key)).lower() == str(value).lower()]
        return result

    def display_books(self) -> None:
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(f"{book.id}: {book.title} "
                  f"Автор: {book.author}, {book.year} - {book.status}")

    def update_book_status(self, book_id: int, status: str) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
