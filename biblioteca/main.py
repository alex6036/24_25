import gradio as gr
from sqlalchemy.orm import Session
from database import init_db, Session
from models import Book, User, BookGenre

# Inicializar la base de datos
init_db()

# Función para añadir libro
def add_book(title, author, genre):
    session = Session()
    new_book = Book(title=title, author=author, genre=BookGenre[genre])
    session.add(new_book)
    session.commit()
    session.close()
    return f"✅ Libro '{title}' añadido."

# Función para añadir usuario
def add_user(name):
    session = Session()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    session.close()
    return f"👤 Usuario '{name}' añadido."

# Función para ver los libros
def list_books():
    session = Session()
    books = session.query(Book).all()
    result = "\n".join([f"{b.title} ({'Disponible' if b.is_available else 'Prestado'})" for b in books])
    session.close()
    return result if result else "No hay libros."

# Función para ver los usuarios
def list_users():
    session = Session()
    users = session.query(User).all()
    result = "\n".join([f"{u.name}" for u in users])
    session.close()
    return result if result else "No hay usuarios."

# Función para prestar libro
def borrow_book(user_name, book_title):
    session = Session()
    user = session.query(User).filter(User.name == user_name).first()
    book = session.query(Book).filter(Book.title == book_title).first()
    
    if user and book:
        if book.is_available:
            book.is_available = False
            session.commit()
            session.close()
            return f"✅ {user_name} ha tomado prestado '{book_title}'."
        else:
            session.close()
            return f"❌ El libro '{book_title}' no está disponible."
    else:
        session.close()
        return "⚠️ Usuario o libro no encontrado."

# Función para devolver libro
def return_book(user_name, book_title):
    session = Session()
    user = session.query(User).filter(User.name == user_name).first()
    book = session.query(Book).filter(Book.title == book_title).first()
    
    if user and book:
        if not book.is_available:
            book.is_available = True
            session.commit()
            session.close()
            return f"📚 {user_name} ha devuelto '{book_title}'."
        else:
            session.close()
            return f"⚠️ El libro '{book_title}' no ha sido prestado."
    else:
        session.close()
        return "⚠️ Usuario o libro no encontrado."

# Interfaz Gradio
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

    with gr.Tab("Ver Usuarios"):
        out4 = gr.Textbox(label="Usuarios en la Biblioteca")
        btn4 = gr.Button("Listar Usuarios")
        btn4.click(fn=list_users, outputs=out4)

    with gr.Tab("Prestar Libro"):
        user_name_borrow = gr.Textbox(label="Nombre del Usuario")
        book_title_borrow = gr.Textbox(label="Título del Libro")
        out5 = gr.Textbox(label="Resultado")
        btn5 = gr.Button("Prestar Libro")
        btn5.click(fn=borrow_book, inputs=[user_name_borrow, book_title_borrow], outputs=out5)

    with gr.Tab("Devolver Libro"):
        user_name_return = gr.Textbox(label="Nombre del Usuario")
        book_title_return = gr.Textbox(label="Título del Libro")
        out6 = gr.Textbox(label="Resultado")
        btn6 = gr.Button("Devolver Libro")
        btn6.click(fn=return_book, inputs=[user_name_return, book_title_return], outputs=out6)

demo.launch(share=True)
