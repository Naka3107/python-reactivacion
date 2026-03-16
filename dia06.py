import requests

def buscar_pais(nombre):

    try:
        respuesta = requests.get(f"https://restcountries.com/v3.1/name/{nombre}")
        if respuesta.status_code!=200:
            print("País no encontrado")
            return None
        datos = respuesta.json()

        pais = datos[0]

        nombre = pais["name"]["common"]
        capital = pais["capital"][0]
        poblacion = pais["population"]
        region = pais["region"]
        idiomas = list(pais["languages"].values())

        dicc_pais = {
            "nombre": nombre,
            "capital": capital,
            "poblacion": poblacion,
            "region": region,
            "idiomas": idiomas
        }
        return dicc_pais
    
    except requests.exceptions.ConnectionError:
        print("Error de conexión")

def comparar_paises(lista_nombres):
    # paises = []
    # for nombre in lista_nombres:
    #     pais = buscar_pais(nombre)
    #     if (pais):
    #         paises.append(pais)
    # paises = [buscar_pais(nombre) for nombre in lista_nombres if buscar_pais(nombre)] CODIGO ORIGINAL pero llama doble a buscar_pais
    paises = [pais for nombre in lista_nombres if (pais := buscar_pais(nombre))] ## Solucion optima usando una funcion walrus, que asigna el valor a la variable directamente
    paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=True)
    print("País            Capital         Población       Idiomas\n----------------------------------------------------------")
    for pais in paises_ordenados:
        poblacion_fmt = f"{pais['poblacion']:,}"
        print(f"{pais["nombre"]:<20}{pais["capital"]:<20}{poblacion_fmt:<20}{pais["idiomas"][0]:<20}")

lista_paises = ["usa","germany","france","brazil"]
comparar_paises(lista_paises)