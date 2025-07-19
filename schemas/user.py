#Código visto en clase

from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    email: str

    class Config:
        orm_mode = True