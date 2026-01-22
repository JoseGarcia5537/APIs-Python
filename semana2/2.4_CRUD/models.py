from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    
    #Relacion de uno a muchos
    tareas: Mapped[list["Task"]] = relationship(
        back_populates="proyecto",
        cascade="all, delete-orphan"
    )

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    completada: Mapped[bool] = mapped_column(default=False)
    
    #Llave foranea
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    
    #Relacion de muchos a uno
    proyecto: Mapped["Project"] = relationship(back_populates="tareas")