from book import Book
from user import User

class Employee:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def add_book(self, biblioteca: list, book: Book):
        biblioteca.append(book)
        print(f"📘 Libro '{book.get_title()}' añadido por {self._name}.")

    def add_user(self, usuarios: list, user: User):
        usuarios.append(user)
        print(f"👤 Usuario '{user.get_name()}' añadido por {self._name}.")
