import os #Para cargar variables de entorno
from dotenv import load_dotenv #Para cargar variables de entorno
import psycopg2
import csv

load_dotenv()

conn = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = os.getenv("DB_PORT")
)

cursor = conn.cursor()

#3.- Creamos una tabla de alumnos
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS empleado (
               id SERIAL PRIMARY KEY,
               nombre VARCHAR(50),
               apellidoP VARCHAR(50),
               apellidoM VARCHAR(50),
               email VARCHAR(100),
               puesto VARCHAR(50),
               contacto VARCHAR(20),
               sexo VARCHAR(20),
               estadoCiv VARCHAR(20)
               );
               """)

with open("registros_personal.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) #Para saltar el encabezado
    
    for row in reader:
        nombre = row[0].strip()
        apellidoP =row[1].strip() 
        apellidoM = row[2].strip()
        email = row[3].strip()
        puesto = row[4].strip()
        contacto = row[5].strip()
        sexo = row[6].strip()
        estadoCiv = row[7].strip()
        
        cursor.execute(
            """
            INSERT INTO empleado (nombre, apellidoP, apellidoM, email, puesto, contacto, sexo, estadoCiv)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, row
        )
        
conn.commit()
cursor.close()
conn.close()

print("CSV importado correctamente")