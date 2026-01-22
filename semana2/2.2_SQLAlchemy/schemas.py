#Martes, esquema pydantic
from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nombre: str
    edad: int
    email: EmailStr
    
class UsuarioResponse(UsuarioCreate):
    id: int
    
    class Config:
        from_attributes = True #Para sql alchemy
        