from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.libro import LibroCreate, LibroOut
from models.libro import Libro
from auth.jwt import get_db, get_current_user
from typing import List

router = APIRouter(prefix="/libros", tags=["libros"])

@router.post("/", response_model=LibroOut)
def crear_libro(data: LibroCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    nuevo = Libro(titulo=data.titulo, autor=data.autor)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[LibroOut])
def listar_libros(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Libro).all()

@router.get("/{id}", response_model=LibroOut)
def obtener_libro(id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    libro = db.query(Libro).filter(Libro.id == id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro