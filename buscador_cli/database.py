import sqlite3
from bolsa import Programador, Oferta

def inicializar_db(conn):
    # Conectar — crea el archivo si no existe
    cursor = conn.cursor()

    # Ejecutar SQL
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS ofertas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario INTEGER NOT NULL,
        pais TEXT,
        capital TEXT
        );
    
    CREATE TABLE IF NOT EXISTS programadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        años_experiencia INTEGER NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS tecnologias_oferta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        oferta_id INTEGER NOT NULL,
        tecnologia TEXT NOT NULL,
        FOREIGN KEY (oferta_id) REFERENCES ofertas(id)
        );
    
    CREATE TABLE IF NOT EXISTS tecnologias_programador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        programador_id INTEGER NOT NULL,
        tecnologia TEXT NOT NULL,
        FOREIGN KEY (programador_id) REFERENCES programadores(id)
        );                   
    """)
    
    #filas = cursor.fetchall()  # devuelve lista de tuplas

def guardar_oferta(oferta, conn):

    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO ofertas (empresa, puesto, salario, pais, capital) VALUES (?, ?, ?, ?, ?)",
    (oferta.empresa, oferta.puesto, oferta.salario, oferta.pais, oferta.capital)
    )
    oferta_id = cursor.lastrowid
    for tecnologia in oferta.tecnologias:
        cursor.execute(
        "INSERT INTO tecnologias_oferta (oferta_id, tecnologia) VALUES (?, ?)",
        (oferta_id, tecnologia)
        )

def guardar_programador(programador,conn):

    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO programadores (nombre, ciudad, años_experiencia) VALUES (?, ?, ?)",
    (programador.nombre, programador.ciudad, programador.años_experiencia)
    )
    programador_id = cursor.lastrowid
    for tecnologia in programador.tecnologias:
        cursor.execute(
        "INSERT INTO tecnologias_programador (programador_id, tecnologia) VALUES (?, ?)",
        (programador_id, tecnologia)
        )

def cargar_ofertas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ofertas")
    ofertas_db = cursor.fetchall()  # devuelve lista de tuplas
    cursor.execute("SELECT * FROM tecnologias_oferta")
    tecnologias_db = cursor.fetchall()
    ofertas = []
    for oferta in ofertas_db:
        tecnologias = []
        for tecnologia in tecnologias_db:
            if(tecnologia[1]==oferta[0]):
                tecnologias.append(tecnologia[2])
        #print (tecnologias)
        ofertas.append(Oferta(oferta[1],oferta[2],oferta[3],tecnologias,oferta[4],oferta[5]))
        #print (ofertas)
    return ofertas

def cargar_programadores(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM programadores")
    programadores_db = cursor.fetchall()
    cursor.execute("SELECT * FROM tecnologias_programador")
    tecnologias_db = cursor.fetchall()
    programadores = []
    for programador in programadores_db:
        tecnologias = []
        for tecnologia in tecnologias_db:
            if(tecnologia[1]==programador[0]):
                tecnologias.append(tecnologia[2])
        programadores.append(Programador(programador[1],programador[2],tecnologias,programador[3]))
    return programadores

def resetear_db(conn):
    conn.executescript("""
        DROP TABLE IF EXISTS tecnologias_oferta;
        DROP TABLE IF EXISTS tecnologias_programador;
        DROP TABLE IF EXISTS ofertas;
        DROP TABLE IF EXISTS programadores;
    """)
    conn.commit()
    
# conn = sqlite3.connect("buscador.db")
# inicializar_db(conn)
# #guardar_oferta(Oferta("Raona", "Python Dev", 26000, ["Python", "Git"],"Germany","Berlin"),conn)
# #guardar_programador(Programador("Carlos","Madrid",["SQL", "Java", "Python"],4),conn)
# ofertas = cargar_ofertas(conn)
# # Guardar cambios y cerrar
# conn.commit()
# conn.close()
