from book import Book

class User:
    def __init__(self, name: str):
        self._name = name
        self._borrowed_books = []

    def get_name(self):
        return self._name

    def get_borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book: Book):
        if book.is_available():
            book.set_availability(False)
            self._borrowed_books.append(book)
            print(f"✅ {self._name} ha tomado prestado '{book.get_title()}'.")
        else:
            print(f"❌ El libro '{book.get_title()}' no está disponible.")

    def return_book(self, book: Book):
        if book in self._borrowed_books:
            book.set_availability(True)
            self._borrowed_books.remove(book)
            print(f"📚 {self._name} ha devuelto '{book.get_title()}'.")
        else:
            print(f"⚠️ {self._name} no tiene prestado el libro '{book.get_title()}'.")
