from book import Book
from book_genre import BookGenre

def buscar_libro_por_titulo(libros, titulo):
    for libro in libros:
        if libro.get_title().lower() == titulo.lower():
            return libro
    return None

def main():
    # Base de datos simulada
    biblioteca = [
        Book("1984", "George Orwell", BookGenre.FICTION),
        Book("Una breve historia del tiempo", "Stephen Hawking", BookGenre.SCIENCE),
        Book("El arte de la guerra", "Sun Tzu", BookGenre.ART)
    ]

    # Pedir al usuario el título del libro
    titulo_buscado = input("Introduce el título del libro que deseas buscar: ")

    # Buscar el libro
    libro_encontrado = buscar_libro_por_titulo(biblioteca, titulo_buscado)

    if libro_encontrado:
        print("\n📚 Libro encontrado:")
        print("Título:", libro_encontrado.get_title())
        print("Autor:", libro_encontrado.get_author())
        print("Género:", libro_encontrado.get_genre().value)
        print("¿Disponible?", libro_encontrado.is_available())
    else:
        print("\n❌ El libro no se encuentra en la biblioteca.")

if __name__ == "__main__":
    main()

