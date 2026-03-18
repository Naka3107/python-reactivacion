from api import buscar_pais

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
        print(f"País: {self.pais}")
        print(f"Capital: {self.capital}")

class Programador:
    def __init__(self, nombre, ciudad, tecnologias, años_experiencia):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tecnologias = tecnologias
        self.años_experiencia = años_experiencia
    
    def agregar_tecnologia(self, tecnologia):
        self.tecnologias.append(tecnologia)
    
    def es_compatible(self, oferta):
        tec_compatibles = []
        for tec in self.tecnologias:
            if tec in oferta.tecnologias:
                tec_compatibles.append(tec)
        return tec_compatibles
    
class BolsaDeEmpleo:
    def __init__(self):
        self.ofertas = []
        self.programadores = []
    
    def agregar_oferta(self, oferta, pais):
        print(f"Añadiendo oferta en {pais}...")
        pais_oferta = buscar_pais(pais)
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