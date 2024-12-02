from library_model import Library
from validate import (validate_title,
                      validate_author,
                      validate_year,
                      validate_status)


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
            title = input("Введите название книги: ")
            title = validate_title(title)
            author = input("Введите автора книги: ")
            author = validate_author(author)
            year_input = input("Введите год издания книги: ")
            if not year_input.isdigit():
                raise ValueError("Год издания книги должен быть числом.")
            year = int(year_input)
            year = validate_year(year)
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)
        elif choice == "3":
            search_by = input("Искать по (title, author, year): ")
            value = input(f"Введите значение для поиска по {search_by}: ")
            books = library.search_books(**{search_by: value})
            if books:
                for book in books:
                    print(f"{book.id}: {book.title} "
                          f"Автор: {book.author}, {book.year} - {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            status = validate_status(status)
            library.update_book_status(book_id, status)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
