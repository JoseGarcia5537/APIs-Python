import os #Para cargar variables de entorno
from dotenv import load_dotenv #Para cargar variables de entorno
import psycopg2

#1.- Conexión a la BD
conn = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = os.getenv("DB_PORT")
)

#2.- Creamos un cursor
cursor = conn.cursor()

#3.- Creamos una tabla de alumnos
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS alumnos (
               id SERIAL PRIMARY KEY,
               nombre VARCHAR(50),
               apellidoP VARCHAR(50),
               apellidoM varchar(50),
               edad SMALLINT
               );
               """)

#4.- Insertamos 3 registros
cursor.execute(
    "INSERT INTO alumnos (nombre, apellidoP, apellidoM, edad) VALUES (%s, %s, %s, %s)",
    ("Jose", "Garcia", "A", 21)
)

cursor.execute(
    "INSERT INTO alumnos (nombre, apellidoP, apellidoM, edad) VALUES (%s, %s, %s, %s)",
    ("Max", "Velasco", "B", 21)
)

cursor.execute(
    "INSERT INTO alumnos (nombre, apellidoP, apellidoM, edad) VALUES (%s, %s, %s, %s)",
    ("Claudio", "Soto", "C", 23)
)

#5.- Gurdamos los cambios
conn.commit()

#6.- Cerramos cursor y conexion
cursor.close()
conn.close()

print("Tabla creada e inserciones realizadas correctamente")
