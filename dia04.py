## REPASO DIA 03 LIST COMPREHENSION

# canciones = [
#     {"titulo": "Clair de Lune", "duracion": 5.2, "reproducciones": 1200},
#     {"titulo": "Nocturne Op.9", "duracion": 4.1, "reproducciones": 980},
#     {"titulo": "Ballade No.1", "duracion": 8.3, "reproducciones": 1500},
#     {"titulo": "Fantasie Impromptu", "duracion": 4.8, "reproducciones": 2100},
# ]

#print(', '.join([cancion['titulo'] for cancion in canciones if cancion['reproducciones']>1000]))

## DIA 04 ##

# Sin manejo de errores — el programa explota
#numero = int("hola")  # ❌ ValueError: invalid literal

# Con manejo de errores — el programa sobrevive
try:
    numero = int("hola")
    print(f"El número es {numero}")
except ValueError:
    print("Eso no es un número válido")

# Puedes capturar varios tipos de error
try:
    lista = [1, 2, 3]
    print(lista[10])        # IndexError
    numero = int("hola")    # ValueError
except ValueError:
    print("Error de valor")
except IndexError:
    print("Índice fuera de rango")
finally:
    print("Esto se ejecuta siempre, haya error o no")
    
canciones = [
    {"titulo": "Clair de Lune", "duracion": 5.2, "reproducciones": 1200},
    {"titulo": "Nocturne Op.9", "duracion": 4.1, "reproducciones": 980},
    {"titulo": "Ballade No.1", "duracion": 8.3, "reproducciones": 1500},
]

def buscar_cancion(lista, titulo):
    if not isinstance(titulo, str):
        print("El título debe ser un string")
        return None
    for cancion in lista:
        if cancion["titulo"] == titulo:
            return cancion
    return None

resultado = buscar_cancion(canciones, "Clair de Lune")
print(resultado["reproducciones"])  # ✅ funciona

resultado = buscar_cancion(canciones, "No existe")
if resultado:
    print(resultado["reproducciones"])
else:
    print("Canción no encontrada")

resultado = buscar_cancion(canciones, 12345)
try:
    print(resultado["reproducciones"])  # ✅ funciona
except TypeError:
    print("Tipo de dato incorrecto\n\n")

# Escribir un archivo
with open("canciones.txt", "w", encoding="utf-8") as archivo:
    for cancion in canciones:
        archivo.write(f"{cancion['titulo']} | {cancion['duracion']} | {cancion['reproducciones']}\n")

canciones_2 = []

try:
    with open("canciones.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            cancion = linea.strip().split(" | ")  # .strip() elimina el \n del final, y rsplit lo divide en lista a partir de un caracter
            diccionario_cancion = {"titulo": cancion[0], "duracion": float(cancion[1]), "reproducciones": int(cancion[2])}
            canciones_2.append(diccionario_cancion)
    
except FileNotFoundError:
    print("Archivo no encontrado")

for cancion in canciones_2:
    print(f"Titulo: {cancion['titulo']} | Duración: {cancion['duracion']} | Reproducciones: {cancion['reproducciones']}")

print(type(canciones_2[0]["duracion"]))
print(type(canciones_2[0]["reproducciones"]))

import json

canciones = [
    {"titulo": "Clair de Lune", "duracion": 5.2, "reproducciones": 1200},
    {"titulo": "Nocturne Op.9", "duracion": 4.1, "reproducciones": 980},
]

# Escribir JSON
with open("canciones.json", "w", encoding="utf-8") as archivo:
    json.dump(canciones, archivo, indent=4, ensure_ascii=False)

# Leer JSON
with open("canciones.json", "r", encoding="utf-8") as archivo:
    canciones_leidas = json.load(archivo)

print(canciones_leidas)