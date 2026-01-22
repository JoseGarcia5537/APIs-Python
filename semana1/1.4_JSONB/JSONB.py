import os #Para cargar variables de entorno
from dotenv import load_dotenv #Para cargar variables de entorno
import psycopg2
import json

load_dotenv()

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
CREATE TABLE IF NOT EXISTS configuraciones (
               id SERIAL PRIMARY KEY,
               usuario VARCHAR(50),
               settings JSONB
               );
               """)

#4.- Insertamos registros

data = {
    "tema": "oscuro",
    "notificaciones": True,
    "idioma": "es",
    "permisos": {
        "admin": False,
        "editor": True
    }
    
}

cursor.execute(""" 
               INSERT INTO configuraciones (usuario, settings)
               VALUES (%s, %s)
               """, ("Jose", json.dumps(data)))


#5.- Gurdamos los cambios
conn.commit()

#5.5 Consultamos
#Usuario con tema oscuro 
cursor.execute("""
               SELECT usuario
               FROM configuraciones
               WHERE settings->>'tema' = %s
               """, ("oscuro",))

resultados = cursor.fetchall()

for fila in resultados:
    print(fila[0])
    
#Usuarios que son admin
cursor.execute("""
               SELECT usuario
               FROM configuraciones
               WHERE settings->'permisos'->>'admin' = 'true'
               """)

print(cursor.fetchall())
    

#6.- Cerramos cursor y conexion
cursor.close()
conn.close()

print("Tabla creada e inserciones realizadas correctamente")
