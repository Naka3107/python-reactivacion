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
