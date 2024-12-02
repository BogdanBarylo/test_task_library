def validate_title(title: str) -> str:
    if not title.strip():
        raise ValueError("Название книги не может быть пустым.")
    return title.strip()


def validate_author(author: str) -> str:
    if not author.strip():
        raise ValueError("Имя автора не может быть пустым.")
    return author.strip()


def validate_year(year: int) -> int:
    if not isinstance(year, int) or year <= 0 or year > 2024:
        raise ValueError("Год издания книги должен быть числом от 1 до 2024.")
    return year


def validate_status(status: str) -> str:
    valid_statuses = ["в наличии", "выдана"]
    if status not in valid_statuses:
        raise ValueError(f"Статус может быть только \
                         {', '.join(valid_statuses)}.")
    return status
