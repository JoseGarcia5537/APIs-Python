from pydantic import BaseModel
from datetime import date
from typing import List

class DeveloperCreate(BaseModel):
    nombre: str
    rol: str
    skills: List[str]
    
class DeveloperResponse(BaseModel):
    id: int
    
    class Config:
        from_attributes = True
        
class ProjectCreate(BaseModel):
    nombre: str
    fecha_inicio: date
    
class ProjectResponse(BaseModel):
    id: int
    
    class Config:
        from_attributes = True