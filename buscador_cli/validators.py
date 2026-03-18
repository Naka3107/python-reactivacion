def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("❌ Este campo no puede estar vacío, inténtalo de nuevo.")

def pedir_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("❌ Introduce un número entero positivo.")

def pedir_lista(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return [item.strip() for item in valor.split(",") if item.strip()]
        print("❌ Introduce al menos una tecnología.")