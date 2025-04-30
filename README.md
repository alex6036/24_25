# 24_25
https://github.com/alex6036/24_25.git
# Biblioteca Digital

Este proyecto es una aplicación de biblioteca digital que permite gestionar libros y usuarios, así como realizar operaciones como añadir libros, añadir usuarios, prestar libros y devolver libros. La interfaz gráfica está construida con [Gradio](https://gradio.app/) y utiliza [SQLAlchemy](https://www.sqlalchemy.org/) para la gestión de la base de datos.

## Características

- **Añadir libros**: Registra nuevos libros en la biblioteca.
- **Añadir usuarios**: Registra nuevos usuarios en el sistema.
- **Listar libros**: Muestra todos los libros disponibles y su estado (disponible o prestado).
- **Listar usuarios**: Muestra todos los usuarios registrados.
- **Prestar libros**: Permite a un usuario tomar prestado un libro.
- **Devolver libros**: Permite a un usuario devolver un libro.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el proyecto:

- Python 3.10 o superior
- Las librerías especificadas en `requirements.txt`:

```txt
gradio>=4.18.0
sqlalchemy>=2.0.28

pip install -r requirements.txt

python biblioteca/main.py