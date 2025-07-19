'''#Esquema reserva

from pydantic import BaseModel

class ReservaCreate(BaseModel):
    libro_id: int

class ReservaOut(BaseModel):
    id: int
    libro_id: int
    reservado: bool

    class Config:
        orm_mode = True'''

from pydantic import BaseModel

class ReservaCreate(BaseModel):
    libro_id: int
    usuario_id: int  # Usuario que hace la reserva

class ReservaOut(BaseModel):
    id: int
    libro_id: int
    usuario_id: int # Usuario que hace la reserva
    reservado: bool

    class Config:
        orm_mode = True
