
# APIs y BD con python.

## Semana 1
## 1.1 Entorno Virtual
### Conceptos clave:
Entorno virtual en pyton: Es un entorno aislado donde se pueden instalar librerias y dependencias sin afectar al Python del sistema ni a otros proyectos, es decir que con esto evitamos conflictos entre proyectos.

### Comandos Clave para un entorno virtual en python.
```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install psycopg2
  pip list
  deactivate
```

### Guardar dependencias, esto es lo más recomendado
```bash
  pip freeze > requirements.txt
  pip install -r requirements.txt
```

### Esto se debe subir al gitignore
```bash
  venv/
```

## 1.2 Bases de datos en PostgreSQL
### Comandos clave en PostgreSQL

#### Entrar, crear BD  y usuario en la BD
```bash
  sudo -u postgres psql
  CREATE DATABASE practica;
  CREATE USER becario WITH PASSWORD '123'; 
  GRANT ALL PRIVILEGES ON DATABASE practica TO becario;
```

### Permisos a la BD por nivel
### DATABASE  →  SCHEMA  →  TABLE
#### Conectarse a la BD
```bash 
  GRANT CONNECT ON DATABASE practica TO becario;
```

#### Permisos sobre tablas:
#### Solo consultar
```bash 
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO becario;
```
#### Consultar y modificar
```bash 
  GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA      
  public TO becario;
```

#### Todo menos borrar
```bash 
  GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA 
  public TO becario;
```

#### Todo incluyendo borrar
```bash 
  GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO 
  becario;
```

#### Permisos sobre futuras tablas
```bash 
  ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE ON TABLES TO becario;
```


#### Todo en la BD
```bash 
  GRANT ALL PRIVILEGES ON DATABASE practica TO becario;
```

## Comandos clave de postgres "Terminal"

### Bases de datos
#### Listar BD
```bash 
  \l
```

#### Listar BD con más detalles
```bash 
  \l+
```

#### Conectarse a la BD
```bash 
  \c practica
```

#### Información de la conexión actual
```bash 
  \conninfo
```

### Usuarios y roles
#### Listar usuarios y roles
```bash 
  \du
```

#### Listar usuarios con permisos
```bash 
  \du+
```
### Esquemas
#### Listar esquemas
```bash 
  \dn
```

#### Listar esquemas con detalles
```bash 
  \l
```

### Tablas
#### Listar tablas
```bash 
  \dt
```

#### Listar tablas con tamaño
```bash 
  \dt+
```

#### Tablas de un esquema especifico
```bash 
  \dt esquema.*
```

### Vistas, secuencias y funciones 
#### Listar vistas
```bash 
  \dv
```

#### Listar secuencias
```bash 
  \ds
```

#### Listar funciones
```bash 
  \df
```

#### Funciones con detalles
```bash 
  \df+
```

### Columnas y estructura
#### Ver estructura de una tabla
```bash 
  \d tabla
```

#### Estructura con tamaño
```bash 
  \d+ tabla
```

### Índices y llaves 
#### Listar indices
```bash 
  \di
```

#### Indices con detalles
```bash 
  \di+ 
```

### Consultas útiles
#### Version de PostgreSQL
```bash 
  SELECT version();
```

#### BD actual
```bash 
  SELECT current_database();
```

#### Usuario actual
```bash 
  SELECT current_user;
```

### Importar / Exportar
#### Ejecutar un archivo SQL
```bash 
  \i archivo.sql 
  \copy tabla FROM 'archivo.csv' CSV HEADER
  \copy tabla TO 'archivo.csv' CSV HEADER
```

### Ayuda y salida
#### Ayuda de comandos psql
```bash 
  \? 
```
#### Salir de psql
```bash 
  \q 
```

## 1.3 Bases de datos con python
### Hacemos uso de la libreria
```bash 
  import psycopg2
```

### Estructura
#### Cónexion a la BD
```bash 
  conn = psycopg2.connect(
    host = "localhost",
    database = "practica",
    user = "becario",
    password = "123",
    port = 5432
  )
```

#### Creamos un cursor
```bash 
  cursor = conn.cursor()
```

#### CRUD 
```bash 
  cursor.execute(
    """
    CREATE, INSERT, DELETE, ETC....
    """
  )
```

#### Guardamos los cambios
```bash 
  conn.commit()
```

#### Cerramos el cursor y la conexión
```bash 
  cursor.close()
  conn.close()
```

## 1.4 JSONB
### Conceptos clave:
Tipo de dato JSONB en PostgreSQL: Es un tipo de dato que permite guardar JSON dentro de una tabla SQL, pero de forma optimizada (se puede indexar y consultar rápido)

Este es ideal para configguraciones, metadatos, preferencias, etc.

#### Cambia la inserción
```bash 
  data = {
    "tema": "oscuro",
    "notificaciones": True,
    "idioma": "es",
    "permisos": {
        "admin": False,
        "editor": True
    } 
}
```

#### Insert
```bash 
  cursor.execute(""" 
    INSERT INTO configuraciones (usuario, settings)
     VALUES (%s, %s)
      """, ("Jose", json.dumps(data)))
```


#### Consulta hardcodeadas
```bash 
  WHERE settings->'permisos'->>'admin' = 'true'
```

#### Consulta con contención JSONB mejor rendimiento
```bash 
  SELECT usuario
FROM configuraciones
WHERE settings @> '{"permisos": {"admin": true}}';
```

#### Consulta jsonb_path_exists
```bash 
  SELECT usuario
FROM configuraciones
WHERE jsonb_path_exists(
    settings,
    '$.permisos.admin ? (@ == true)'
);
```

## 1.5 CSV a BD
### Hacemos uso de la libreria
```bash 
  import csv
```

