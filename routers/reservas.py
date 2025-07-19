#Router para reservas

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.reserva import ReservaCreate, ReservaOut
from models.reserva import Reserva
from auth.jwt import get_db, get_current_user
from typing import List

router = APIRouter(prefix="/reservas", tags=["reservas"])

@router.post("/", response_model=ReservaOut)
def crear_reserva(data: ReservaCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if db.query(Reserva).filter(Reserva.libro_id == data.libro_id, Reserva.reservado == True).first():
        raise HTTPException(status_code=400, detail="El libro ya está reservado")

    nueva = Reserva(libro_id=data.libro_id, reservado=True)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=List[ReservaOut])
def listar_reservas(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Reserva).all()


@router.post("/devolver/{id}", response_model=ReservaOut)
def devolver_reserva(id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    reserva = db.query(Reserva).filter(Reserva.id == id, Reserva.reservado == True).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada o ya devuelta")

    reserva.reservado = False
    db.commit()
    db.refresh(reserva)
    return reserva