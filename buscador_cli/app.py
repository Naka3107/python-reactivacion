from flask  import Flask, jsonify, request
import sqlite3
import sys
sys.path.append(".")
from database import cargar_ofertas, cargar_programadores, guardar_oferta, guardar_programador, inicializar_db, resetear_db
from bolsa import Oferta, Programador, BolsaDeEmpleo

app = Flask(__name__)

def get_conn():
    return sqlite3.connect("buscador.db")
    
@app.route("/")
def iniciar():
    return "API corriendo"

@app.route("/ofertas", methods=["GET"])
def get_ofertas():
    conn = get_conn()
    ofertas = cargar_ofertas(conn)
    conn.close()
    resultados = [vars(oferta) for oferta in ofertas]
    return jsonify(resultados)

@app.route("/programadores", methods=["GET"])
def get_programadores():
    conn = get_conn()
    programadores = cargar_programadores(conn)
    conn.close()
    resultados = [vars(programador) for programador in programadores]
    return jsonify(resultados)

@app.route("/ofertas", methods=["POST"])
def post_ofertas():
    datos = request.get_json()
    conn = get_conn()
    for oferta in datos:
        guardar_oferta(Oferta(**oferta),conn)
    conn.commit()
    conn.close()
    return "Ofertas añadidas"

@app.route("/programadores", methods=["POST"])
def post_programadores():    
    datos = request.get_json()
    conn = get_conn()
    for programador in datos:
        guardar_programador(Programador(**programador),conn)
    conn.commit()
    conn.close()
    return "Programadores añadidos"
    
@app.route("/ofertas/compatibles/<nombre>/<int:salario_minimo>", methods=["GET"])
def get_compatibles(nombre, salario_minimo):
    bolsa = BolsaDeEmpleo()
    conn = get_conn()
    bolsa.programadores = cargar_programadores(conn)
    bolsa.ofertas = cargar_ofertas(conn)
    ## Busca al programador
    programador_obj = next((p for p in bolsa.programadores if p.nombre==nombre),None)
    if not programador_obj:
        return "Programador no encontrado", 404
    ## Busca compatibilidades
    resultados = bolsa.buscar_ofertas(programador_obj, salario_minimo) # resultados es una lista de: {"datos_oferta": <objeto Oferta>, "coincidencias": ["Python", "SQL"]}

    ## Hay que cambiarlo los objetos a diccionarios para poder mostrarlo en JSON.
    # En comentario versión completa, en codigo en one liner usando list comprehension:

    # lista_final = []
    # for r in resultados:
    #     oferta_obj = r["datos_oferta"]    # aquí es un objeto Oferta
    #     oferta_dicc = vars(oferta_obj)    # ahora es un diccionario
    #     coincidencias = r["coincidencias"]   # ya es una lista no necesita conversión
        
    #     dicc_final={
    #         "datos_oferta" : oferta_dicc,
    #         "coincidencias" : coincidencias
    #     }
    #     lista_final.append(dicc_final)
    # conn.close()
    # return jsonify(lista_final)

    return jsonify ([{
        "oferta" : vars(r["datos_oferta"]),        # Cambia el objeto a diccionario y lo guarda
        "coincidencias": r["coincidencias"]
    } for r in resultados])
    
@app.route("/reset", methods=["POST"])
def reset_db():
    conn = get_conn()
    resetear_db(conn)
    inicializar_db(conn)
    conn.close()
    return "Base de datos reseteada"

if __name__ == "__main__":
    app.run(debug=True)