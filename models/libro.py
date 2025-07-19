#Código modelo para los libros, se podrían agregar más atributos como el año del libro, etc.

from sqlalchemy import Column, Integer, String
from database import Base

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)