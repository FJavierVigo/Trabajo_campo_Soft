import math
def validar_texto_no_vacio(texto: str) -> bool:
    return len(texto.strip()) > 0

def validar_numero_positivo(valor: float) -> bool:
    return math.isfinite(valor) and valor > 0

def codigo_existe(lotes: list, codigo: str) -> bool:
    for lote in lotes:
        if lote["codigo"].upper() == codigo.strip().upper():
            return True
    return False

def pedir_texto(mensaje: str) -> str:
    while True:
        dato = input(mensaje).strip()
        if validar_texto_no_vacio(dato):
            return dato
        print("  [Error] Este campo no puede estar vacío.")

def pedir_float_positivo(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if validar_numero_positivo(valor):
                return valor
            print("  [Error] El valor debe ser mayor que cero.")
        except ValueError:
            print("  [Error] Ingrese un número válido.")
