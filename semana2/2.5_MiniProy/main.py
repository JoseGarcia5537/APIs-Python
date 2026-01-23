from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Developer, Project
from schemas import DeveloperCreate, DeveloperResponse, ProjectCreate, ProjectResponse

app = FastAPI()

#Esto solo va en el desarrollo 
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
        
@app.post("/developers/", response_model=DeveloperResponse)
def crear_developer(developer: DeveloperCreate, db: Session = Depends(get_db)):
    nuevo = Developer(**developer.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/developers", response_model=list[DeveloperResponse]) 
def listar_developers(db: Session = Depends(get_db)):
    
    return db.query(Developer).all()

@app.post("/projects", response_model=ProjectResponse)
def crear_project(project: ProjectCreate, db: Session = Depends(get_db)):
    nuevo = Project(**project.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/projects", response_model=list[ProjectResponse])
def listar_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@app.post("/assign-developer")
def asignar_developer(
    developer_id: int,
    project_id: int,
    db: Session = Depends(get_db)
):
    developer = db.query(Developer).filter(Developer.id == developer_id).first()
    project = db.query(Project).filter(Project.id == project_id).first()
    
    if not developer or not project:
        raise HTTPException(status_code=404, detail="Developer or Project not found")
    
    project.developers.append(developer)
    db.commit()
    
    return {"message": "Developer assigned to project successfully"}

#Para el reporte 
@app.get("/report/python-projects")
def proyectos_con_python(db: Session = Depends(get_db)):
    projects = db.query(Project).join(Project.developers).filter(Developer.skills.contains(['Python'])).all()
    
    return projects