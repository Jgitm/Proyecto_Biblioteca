#Esquema para los libros

from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str

class LibroOut(BaseModel):
    id: int
    titulo: str
    autor: str

    class Config:
        orm_mode = True