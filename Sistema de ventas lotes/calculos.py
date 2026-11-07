def calcular_precio_total(area: float, precio_m2: float) -> float:
    return round(area * precio_m2, 2)

def calcular_cuota_inicial(precio_total: float, porcentaje: float = 0.20) -> float:
    return round(precio_total * porcentaje, 2)

def calcular_saldo(precio_total: float, cuota_inicial: float) -> float:
    return round(precio_total - cuota_inicial, 2)