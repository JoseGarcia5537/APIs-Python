"""Rutas básicas de la API con FastAPI.

Este módulo define un modelo de datos `Usuario` con Pydantic y dos
endpoints sencillos: uno para verificar que la API está activa y
otro para crear (simular la creación de) un usuario.
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr  # Validación de tipos y email

# Instancia principal de la aplicación FastAPI
app = FastAPI()


# Modelo de datos con Pydantic que representa un usuario.
# Pydantic valida tipos y formatos (por ejemplo, `EmailStr` fuerza un email válido).
class Usuario(BaseModel):
    nombre: str  
    edad: int    
    email: EmailStr 


# Endpoint GET raíz: comprueba que la API está funcionando.
@app.get("/")
def inicio():
    # Devuelve un JSON con un mensaje de estado.
    return {"mensaje": "API funcionando correctamente"}


# Endpoint POST para crear un usuario.
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario creado correctamente",
        "datos": usuario
    }


