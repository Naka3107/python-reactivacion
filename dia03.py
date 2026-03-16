import json
import dia06

class Oferta:
    def __init__(self, empresa, puesto, salario, tecnologias, pais="", capital=""):
        self.empresa = empresa
        self.puesto = puesto
        self.salario = salario
        self.tecnologias = tecnologias
        self.pais = pais
        self.capital = capital

    def mostrar(self):
        print(f"--- {self.empresa} ---")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: {self.salario}€/año")
        print(f"Tecnologías: {self.tecnologias}")

class Programador:
    def __init__(self, nombre, ciudad, tecnologias, años_experiencia):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tecnologias = tecnologias
        self.años_experiencia = años_experiencia
    
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Tecnologias: {', '.join(self.tecnologias)}") ## Usas string.join(lista) para imprimir todo el contenido de una lista separados por el string que indicaste
        print(f"Años de experiencia: {self.años_experiencia}")

    def agregar_tecnologia(self, tecnologia):
        self.tecnologias.append(tecnologia)
    
    def es_compatible(self, oferta):
        tec_compatibles = []
        for tec in self.tecnologias:
            if tec in oferta.tecnologias:
                tec_compatibles.append(tec)
        return tec_compatibles

class ProgramadorFreelance(Programador):
    def __init__(self, nombre, ciudad, tecnologias, años_experiencia, tarifa_hora):
        super().__init__(nombre, ciudad, tecnologias, años_experiencia)     
        self.tarifa_hora = tarifa_hora
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def calcular_ingreso_mensual(self, horas_mes):
        return self.tarifa_hora * horas_mes
    
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Tarifa por hora: {self.tarifa_hora}")
        print(f"Clientes: {', '.join(self.clientes)}")

class BolsaDeEmpleo:
    def __init__(self):
        self.ofertas = []
        self.programadores = []
    
    def agregar_oferta(self, oferta, pais):
        print(f"Añadiendo oferta en {pais}...")
        pais_oferta = dia06.buscar_pais(pais)
        if(pais_oferta):
            print(f"País verificado: {pais_oferta["nombre"]} | Capital: {pais_oferta["capital"]} | Región: {pais_oferta["region"]}")
            oferta.pais = pais_oferta["nombre"]
            oferta.capital = pais_oferta["capital"]
            self.ofertas.append(oferta)
        else:
            print("País no encontrado - oferta no añadida")

    
    def agregar_programador(self, programador):
        self.programadores.append(programador)

    def buscar_ofertas(self, programador, salario_minimo):
        ofertas_probables = []
        if programador in self.programadores:
            for oferta in self.ofertas:
                coincidencias = programador.es_compatible(oferta)
                if coincidencias and oferta.salario>salario_minimo:
                    ofertas_probables.append({
                        "datos_oferta" : oferta,
                        "coincidencias" : coincidencias 
                    })
            return sorted(ofertas_probables, key=lambda oferta_probable : oferta_probable["datos_oferta"].salario, reverse=True)
        else:
            print("Programador no registrado")
            return False
        
    def guardar(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                lista_dicts = [vars(oferta) for oferta in self.ofertas]
                json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            print("Archivo no encontrado")
        
    def cargar(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                ofertas = json.load(archivo)
                for oferta in ofertas:
                    #self.agregar_oferta(Oferta(oferta["empresa"], oferta["puesto"], oferta["salario"], oferta["tecnologias"])) ## Manualmente tienes que poner todos los atributos
                    #self.agregar_oferta(Oferta(**oferta),oferta["pais"]) ## Cuando todos los atributos coinciden, automáticamente lo convierte a objeto       
                    self.ofertas.append(Oferta(**oferta))  # Carga directa, sin API       
        except FileNotFoundError:
            print("Archivo no encontrado")
    
    def exportar_reporte(self, programador, salario_minimo):
        try:
            with open("reporte.json", "w", encoding="utf-8") as archivo:
                dicc_ofertas = self.buscar_ofertas(programador, salario_minimo)
                if dicc_ofertas:
                    ofertas_compatibles = []
                    for oferta in dicc_ofertas:
                        oferta_compatible = {
                            "empresa":  oferta["datos_oferta"].empresa,
                            "puesto":  oferta["datos_oferta"].puesto,
                            "salario": oferta["datos_oferta"].salario,
                            "coincidencias": oferta["coincidencias"]
                        }
                        ofertas_compatibles.append(oferta_compatible)
                    #print(ofertas_compatibles)
                    datos_json = {
                        "programador": programador.nombre,
                        "salario_minimo": salario_minimo,
                        "ofertas_compatibles": ofertas_compatibles
                    }
                    json.dump(datos_json, archivo, indent=4, ensure_ascii=False)
                else:
                    print("No se puede generar archivo, programador no existe")
        except FileNotFoundError:
            print("Archivo no encontrado")
    
    def exportar_txt(self):
        try:
            with open("ofertas.txt","w",encoding="utf-8") as archivo:
                for oferta in self.ofertas:
                    archivo.write(f"{oferta.empresa} | {oferta.puesto} | {oferta.salario}\n")
        except FileNotFoundError:
            print("Archivo no encontrado")        

bolsa = BolsaDeEmpleo()
bolsa.agregar_oferta(Oferta("Raona", "Python Dev", 26000, ["Python", "Git"]),"Germany")
bolsa.agregar_oferta(Oferta("Sopra", "Backend Junior", 22000, ["Java", "SQL"]),"France")

bolsa.guardar("ofertas_enriquecidas.json")

bolsa2 = BolsaDeEmpleo()
bolsa2.cargar("ofertas_enriquecidas.json")
#for oferta in bolsa2.ofertas:
#    oferta.mostrar()

# bolsa = BolsaDeEmpleo()
# bolsa.agregar_oferta(Oferta("Raona", "Python Dev", 26000, ["Python", "Git"]))
# bolsa.agregar_oferta(Oferta("Sopra", "Backend Junior", 28000, ["Java", "SQL"]))
# bolsa.agregar_oferta(Oferta("Deloitte", "Fullstack", 20000, ["Python", "Docker"]))

carlos = Programador("Carlos", "Barcelona", ["Python", "SQL", "Git"], 0)
bolsa.agregar_programador(carlos)

bolsa.exportar_reporte(carlos, 19000)
bolsa.exportar_txt()
# resultados = bolsa.buscar_ofertas(carlos, 19000)
# for resultado in resultados:
#     print(f"✓ {resultado['datos_oferta'].empresa} | {resultado['datos_oferta'].salario}€ | coincide en: {resultado['coincidencias']}")

#oferta = Oferta("Raona", "Python Developer", 26000, ["Python", "Java"])
#print(carlos.es_compatible(oferta))

# canciones = [
#     {"titulo": "Clair de Lune", "duracion": 5.2, "reproducciones": 1200},
#     {"titulo": "Nocturne Op.9", "duracion": 4.1, "reproducciones": 980},
#     {"titulo": "Ballade No.1", "duracion": 8.3, "reproducciones": 1500},
#     {"titulo": "Fantasie Impromptu", "duracion": 4.8, "reproducciones": 2100},
# ]

# canciones_por_duracion = sorted(canciones, key = lambda cancion: cancion["duracion"])
# canciones_por_reproduccion = sorted(canciones, key = lambda cancion: cancion["reproducciones"], reverse=True)
# canciones_por_titulo = sorted(canciones, key = lambda cancion: cancion["titulo"])

# print(f"Ordenadas por Duracion: {', '.join([cancion['titulo'] for cancion in canciones_por_duracion])}")
# print(f"Ordenadas por Reproduccion: {', '.join([cancion['titulo'] for cancion in canciones_por_reproduccion])}")
# print(f"Ordenadas por Titulo: {', '.join([cancion['titulo'] for cancion in canciones_por_titulo])}")

