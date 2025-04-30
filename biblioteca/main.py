from book import Book
from book_genre import BookGenre
from user import User
from employee import Employee

def main():
    # Inicializar listas vacías
    biblioteca = []
    usuarios = []

    # Crear un empleado
    empleado = Employee("Laura")

    # Crear libros y agregarlos con el empleado
    libro1 = Book("1984", "George Orwell", BookGenre.FICTION)
    libro2 = Book("El arte de la guerra", "Sun Tzu", BookGenre.ART)

    empleado.add_book(biblioteca, libro1)
    empleado.add_book(biblioteca, libro2)

    # Crear un usuario y añadirlo con el empleado
    usuario1 = User("Carlos")
    empleado.add_user(usuarios, usuario1)

    print("\n📚 Libros en la biblioteca:")
    for libro in biblioteca:
        print(f"- {libro.get_title()} ({'Disponible' if libro.is_available() else 'Prestado'})")

    # Usuario toma prestado un libro
    print("\n📥 Préstamo de libro:")
    usuario1.borrow_book(libro1)

    # Usuario intenta tomar el mismo libro otra vez
    usuario1.borrow_book(libro1)

    # Usuario devuelve el libro
    print("\n📤 Devolución de libro:")
    usuario1.return_book(libro1)

    # Usuario intenta devolverlo otra vez
    usuario1.return_book(libro1)

if __name__ == "__main__":
    main()

