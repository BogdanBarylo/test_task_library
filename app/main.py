from app.library_model import Library
from app.validate import (validate_title,
                          validate_author,
                          validate_year,
                          validate_status)


def display_books(books):
    """Отображает список книг."""
    if not books:
        print("Библиотека пуста.")
    else:
        for book in books:
            print(f"{book.id}: {book.title} "
                  f"Автор: {book.author}, {book.year} - {book.status}")


def main():
    library = Library()
    while True:
        print("\n--- Меню ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                title = validate_title(input("Введите название книги: "))
                author = validate_author(input("Введите автора книги: "))
                year = validate_year(int(input("Введите год издания книги: ")))
                new_book = library.add_book(title, author, year)
                print(f"Книга '{new_book.title}' добавлена с ID {new_book.id}.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
                print(f"Книга с ID {book_id} удалена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            search_by = input("Искать по (title, author, year): ")
            value = input(f"Введите значение для поиска по {search_by}: ")
            books = library.search_books(**{search_by: value})
            if books:
                display_books(books)
            else:
                print("Книги не найдены.")

        elif choice == "4":
            display_books(library.books)

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: "))
                status = validate_status(
                    input("Введите новый статус ('в наличии' или 'выдана'): "))
                library.update_book_status(book_id, status)
                print(f"Статус книги с ID {book_id} обновлён на '{status}'.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
