from book import Book
from book_genre import BookGenre

def main():
    # Crear un libro
    libro = Book("1984", "George Orwell", BookGenre.FICTION)

    # Mostrar información del libro
    print("Título:", libro.get_title())
    print("Autor:", libro.get_author())
    print("Género:", libro.get_genre().value)
    print("¿Está disponible?", libro.is_available())

    # Marcar como prestado
    libro.set_availability(False)
    print("¿Está disponible después del préstamo?", libro.is_available())

if __name__ == "__main__":
    main()
