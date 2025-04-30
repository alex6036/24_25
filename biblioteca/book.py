from book_genre import BookGenre
import gradio as gr

with gr.Blocks() as demo:
    nombre = gr.Textbox(label="Tu nombre")
    salida = gr.Textbox(label="Saludo")
    btn = gr.Button("Saludar")

    def saludar(nombre):
        return f"Hola, {nombre}!"

    btn.click(saludar, inputs=nombre, outputs=salida)

demo.launch()


class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_available = True  # Por defecto, el libro está disponible
    # Getters
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def is_available(self):
        return self._is_available

    # Setters
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_genre(self, genre: BookGenre):
        self._genre = genre

    def set_availability(self, status: bool):
        self._is_available = status
