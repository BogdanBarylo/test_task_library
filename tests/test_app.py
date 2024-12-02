import pytest
from exception import BookNotFoundError
from library_model import Library
from validate import (validate_title,
                      validate_author,
                      validate_year,
                      validate_status)


def test_add_book(library):
    library.add_book("Война и мир", "Лев Толстой", 1869)
    library.add_book("Анна Каренина", "Лев Толстой", 1877)
    assert len(library.books) == 2
    assert library.books[0].title == "Война и мир"
    assert library.books[1].author == "Лев Толстой"


def test_remove_nonexistent_book(library):
    library.add_book("Война и мир", "Лев Толстой", 1869)
    with pytest.raises(BookNotFoundError, match="Книга с ID 99 не найдена."):
        library.remove_book(99)

def test_update_book_status_invalid_id(library):
    library.add_book("Война и мир", "Лев Толстой", 1869)
    with pytest.raises(BookNotFoundError, match="Книга с ID 99 не найдена."):
        library.update_book_status(99, "выдана")


def test_search_books_multiple_criteria(library):
    library.add_book("Война и мир", "Лев Толстой", 1869)
    library.add_book("Анна Каренина", "Лев Толстой", 1877)
    results = library.search_books(author="Лев Толстой", year=1869)
    assert len(results) == 1
    assert results[0].title == "Война и мир"


def test_save_and_load_books(library):
    library.add_book("Война и мир", "Лев Толстой", 1869)
    library.save_books()
    new_library = Library(file_path="test_library.json")
    assert len(new_library.books) == 1
    assert new_library.books[0].title == "Война и мир"


def test_validate_title():
    assert validate_title("Война и мир") == "Война и мир"
    with pytest.raises(ValueError):
        validate_title("")
    with pytest.raises(ValueError):
        validate_title("   ")


def test_validate_author():
    assert validate_author("Лев Толстой") == "Лев Толстой"
    with pytest.raises(ValueError):
        validate_author("")
    with pytest.raises(ValueError):
        validate_author("   ")


def test_validate_year():

    assert validate_year(2023) == 2023
    assert validate_year(1) == 1
    with pytest.raises(ValueError):
        validate_year(0)
    with pytest.raises(ValueError):
        validate_year(3000)
    with pytest.raises(ValueError):
        validate_year(-10)


def test_validate_status():
    assert validate_status("в наличии") == "в наличии"
    assert validate_status("выдана") == "выдана"
    with pytest.raises(ValueError):
        validate_status("неизвестный статус")
    with pytest.raises(ValueError):
        validate_status("")
