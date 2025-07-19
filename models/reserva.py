'''#Modelo reserva

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from database import Base

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), unique=True) #ForeignKey("libros.id") crea una relación en la base para que este valor solo pueda ser un id válido de la tabla libros
    reservado = Column(Boolean, default=True)'''

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from database import Base

class Reserva(Base):
    __tablename__ = "reservas"
    
    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), unique=True) #ForeignKey("libros.id") crea una relación en la base para que este valor solo pueda ser un id válido de la tabla libros
    usuario_id = Column(Integer, ForeignKey("users.id"))
    reservado = Column(Boolean, default=True)
