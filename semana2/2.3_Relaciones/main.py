from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Project, Task
from schemas import ProjectCreate, ProjectResponse, TaskCreate, TaskResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Ver si api funciona
@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}
        
#Creamos proyecto
@app.post("/projects", response_model=ProjectResponse)
def crear_proyecto(proyecto: ProjectCreate, db: Session = Depends(get_db)):
    nuevo = Project(nombre=proyecto.nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

#Creamos tarea para proyecto
@app.post("/projects/{project_id}/tasks", response_model=TaskResponse)
def crear_tarea(
    project_id: int,
    tarea: TaskCreate,
    db: Session = Depends(get_db)
):
    nueva = Task(
        titulo=tarea.titulo,
        project_id=project_id
    )
    
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

#Vemos proyecto con sus tareas
@app.get("/projects/{project_id}", response_model=ProjectResponse)
def ver_proyecto(
    project_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Project).filter(Project.id == project_id).first()

