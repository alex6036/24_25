from book_genre import BookGenre

class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_available = True  # Por defecto, el libro está disponible
