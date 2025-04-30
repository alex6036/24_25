import gradio as gr
from sqlalchemy.orm import Session
from database import Session, init_db
from models import Book, User, BookGenre

init_db()

def add_book(title, author, genre):
    session = Session()
    new_book = Book(title=title, author=author, genre=BookGenre[genre])
    session.add(new_book)
    session.commit()
    session.close()
    return f"✅ Libro '{title}' añadido."

def add_user(name):
    session = Session()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    return f"👤 Usuario '{name}' añadido."

def list_books():
    session = Session()
    books = session.query(Book).all()
    result = "\n".join([f"{b.title} ({'Disponible' if b.is_available else 'Prestado'})" for b in books])
    session.close()
    return result if result else "No hay libros."

with gr.Blocks() as demo:
    with gr.Tab("Añadir Libro"):
        title = gr.Textbox(label="Título")
        author = gr.Textbox(label="Autor")
        genre = gr.Dropdown(choices=[g.name for g in BookGenre], label="Género")
        out1 = gr.Textbox(label="Resultado")
        btn1 = gr.Button("Añadir Libro")
        btn1.click(fn=add_book, inputs=[title, author, genre], outputs=out1)

    with gr.Tab("Añadir Usuario"):
        username = gr.Textbox(label="Nombre de Usuario")
        out2 = gr.Textbox(label="Resultado")
        btn2 = gr.Button("Añadir Usuario")
        btn2.click(fn=add_user, inputs=[username], outputs=out2)

    with gr.Tab("Ver Libros"):
        out3 = gr.Textbox(label="Libros en Biblioteca")
        btn3 = gr.Button("Listar Libros")
        btn3.click(fn=list_books, outputs=out3)

demo.launch()
