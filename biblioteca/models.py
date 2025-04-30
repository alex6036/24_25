from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class BookGenre(enum.Enum):
    FICTION = "Fiction"
    NONFICTION = "Nonfiction"
    SCIENCE = "Science"
    ART = "Art"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(Enum(BookGenre))
    is_available = Column(Boolean, default=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
