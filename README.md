# Library Manager

## Описание

**Library Manager** — это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и изменять статус книг. Данные хранятся в формате JSON, что обеспечивает их простое сохранение и загрузку.

---

## Возможности

- **Добавление книг**: Введите название, автора и год издания книги. Программа добавит книгу с уникальным ID и статусом "в наличии".
- **Удаление книг**: Удалите книгу по её ID.
- **Поиск книг**: Ищите книги по названию, автору или году издания.
- **Отображение всех книг**: Выводит список всех книг с их ID, названием, автором, годом и статусом.
- **Изменение статуса книги**: Установите статус "в наличии" или "выдана" для книги по её ID.

---

## Установка и запуск

1. **Клонирование репозитория**:
   ```bash
   git clone git@github.com:BogdanBarylo/test_task_library.git
    ```
2. **Установка зависимостей**
    ```bash 
    pip install -r requirements.txt
    ```
3. **Запуск приложения**
    ```bash
    python main.py
    ```
---
## Использование

    --- Меню ---
    1. Добавить книгу
    2. Удалить книгу
    3. Искать книгу
    4. Показать все книги
    5. Изменить статус книги
    0. Выход
    Введите номер действия:


1. ***Добавление книги:***:

    Введите название книги: Война и мир
    Введите автора книги: Лев Толстой
    Введите год издания книги: 1869
    Книга 'Война и мир' добавлена с ID 1.

2. ***Удаление книги***:

    Введите ID книги для удаления: 1
    Книга с ID 1 удалена.

3. ***Поиск книги***:

    Искать по (title, author, year): title
    Введите значение для поиска по title: Война и мир
    1: Война и мир Автор: Лев Толстой, 1869 - в наличии

4. ***Отображение всех книг***:

    1: Война и мир Автор: Лев Толстой, 1869 - в наличии
    2: Преступление и наказание Автор: Федор Достоевский, 1866 - выдана

5. ***Изменение статуса книги***:

    Введите ID книги: 2
    Введите новый статус ('в наличии' или 'выдана'): в наличии
    Статус книги с ID 2 обновлен на 'в наличии'.
