##### REPASO DIA 01 ######
def dame_tecnologias():

    tecnologias = ["PHP","SQL","Angular","JavaScript","Node"]
    for i, v in enumerate(tecnologias):
        print(f"{i+1}. {v}")

dame_tecnologias()

##### Dia 02 ####

oferta_trabajo = {
    "empresa": "Sopra Steria",
    "puesto": "Backend Developer Junior",
    "ciudad": "Barcelona",
    "salario": 22000,
    "tecnologias": ["Java","Spring Boot","SQL"],
    "remoto": False
}

print(f"--- Oferta de Trabajo ---\nEmpresa: {oferta_trabajo['empresa']}")
print(f"Puesto: {oferta_trabajo['puesto']}")
print(f"Ciudad: {oferta_trabajo['ciudad']}")
print(f"Salario: {oferta_trabajo['salario']}€/año")
print(f"Remoto: {oferta_trabajo['remoto']}")
print(f"Tecnologías :")
for i, tec in enumerate(oferta_trabajo["tecnologias"]):
    print(f"{i+1}. {tec}")

##########################

def es_compatible(mis_tecnologias, oferta):
    tec_compatibles = []
    for tec in mis_tecnologias:
        if tec in oferta["tecnologias"]:
            tec_compatibles.append(tec)
    return tec_compatibles

mis_tecnologias = ["PHP", "Angular", "Node"]
resultado = es_compatible(mis_tecnologias, oferta_trabajo)
print(f"¿Soy compatible con la oferta? {resultado}")

################################

oferta_1 = {
    "empresa": "Sopra Steria",
    "puesto": "Backend Developer Junior",
    "ciudad": "Barcelona",
    "salario": 22000,
    "tecnologias": ["Node","Angular","C"],
    "remoto": False
}

oferta_2 = {
    "empresa": "Raona",
    "puesto": "Python Developer",
    "ciudad": "Barcelona",
    "salario": 26000,
    "tecnologias": ["PHP","C++","Python"],
    "remoto": True
}

oferta_3 = {
    "empresa": "Deloitte",
    "puesto": "Fullstack Developer",
    "ciudad": "Cadiz",
    "salario": 20000,
    "tecnologias": ["Java","Spring Boot","SQL"],
    "remoto": True
}

lista_ofertas = [oferta_1, oferta_2, oferta_3]

print("--- Ofertas compatibles ---")
for oferta in lista_ofertas:
    if es_compatible(mis_tecnologias, oferta):
        print(f"✓ {oferta['empresa']} - {oferta['puesto']} ({oferta['salario']}€/año)")

mis_tecnologias = ["Python", "SQL", "Git"]

for oferta in lista_ofertas:
    coincidencias = es_compatible(mis_tecnologias, oferta)
    if coincidencias:
        print(f"✓ {oferta['empresa']} - coincide en: {coincidencias}")

def filtrar_ofertas(lista_ofertas, tecnologias, salario_minimo):
    ofertas_viables = []
    for oferta in lista_ofertas:
        coincidencias = es_compatible(tecnologias, oferta)
        if coincidencias and oferta["salario"]>salario_minimo:
            ofertas_viables.append({
                "datos_oferta": oferta,
                "coincidencias": coincidencias
                })
    return sorted(ofertas_viables, key=lambda oferta_viable : oferta_viable["datos_oferta"]["salario"], reverse=True) 
    ## Funcion lambda te deja recorrer la libreria declarando una variable rapida. Como es un diccionario dentro
    ## un diccionario, tengo que entrar doble, entrando al salario guardado en los datos de cada oferta
            
ofertas_finales = filtrar_ofertas(lista_ofertas, mis_tecnologias,19000)
print("--- Ofertas filtradas ---")
for resultado in ofertas_finales:
    print(f"✓ {resultado['datos_oferta']['empresa']} - {resultado['datos_oferta']['puesto']} | {resultado['datos_oferta']['salario']}€ | coincide en: {resultado['coincidencias']}")