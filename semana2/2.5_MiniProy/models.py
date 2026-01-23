from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database import Base

# Tabla intermedia para las asignaciones
project_developer = Table(
    "project_developer", Base.metadata,
    Column("developer_id", ForeignKey("developers.id"), primary_key=True),
    Column("project_id", ForeignKey("projects.id"), primary_key=True)
)

class Developer(Base):
    __tablename__ = "developers"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    rol = Column(String, nullable=False)
    skills = Column(JSONB, nullable=False)
    
    projects = relationship(
        "Project",
        secondary=project_developer,
        back_populates="developers"
    )
    
class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    
    developers = relationship(
        "Developer",
        secondary=project_developer,
        back_populates="projects"
    )