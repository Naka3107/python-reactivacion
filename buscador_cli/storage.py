import json
from bolsa import Oferta

def guardar_ofertas(ofertas, nombre_archivo):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            lista_dicts = [vars(oferta) for oferta in ofertas]
            json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("Archivo no encontrado")

def cargar_ofertas(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            ofertas = json.load(archivo)
            lista_ofertas = []
            for oferta in ofertas:
                lista_ofertas.append(Oferta(**oferta))
            return lista_ofertas
    except FileNotFoundError:
        print("Archivo no encontrado")
        return []