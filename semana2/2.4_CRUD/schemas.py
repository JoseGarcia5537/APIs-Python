from pydantic import BaseModel
from typing import List

class TaskCreate(BaseModel):
    titulo: str
    
class TaskResponse(TaskCreate):
    id: int
    completada: bool
    
    class Config:
        from_attributes = True
        
class ProjectCreate(BaseModel):
    nombre: str
    
class ProjectResponse(ProjectCreate):
    id: int 
    tareas: List[TaskResponse] = []
    
    class Config:
        from_attributes = True
        
##Se agrega el dia jueves 
class TaskUpdate(BaseModel):
    completada: bool