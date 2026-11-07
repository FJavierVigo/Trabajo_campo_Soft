import calculos
import validaciones

def registrar_lote(lotes: list):
    print("\n--- REGISTRAR NUEVO LOTE ---")
    codigo = validaciones.pedir_texto("Código del lote (ej. LT-001): ").upper()
    
    if validaciones.codigo_existe(lotes, codigo):
        print(f"  [Error] El código '{codigo}' ya está registrado.")
        return

    urbanizacion = validaciones.pedir_texto("Urbanización: ")
    area = validaciones.pedir_float_positivo("Área (m2): ")
    precio_m2 = validaciones.pedir_float_positivo("Precio por m2 (S/): ")
    precio_total = calculos.calcular_precio_total(area, precio_m2)

    nuevo_lote = {
        "codigo": codigo,
        "urbanizacion": urbanizacion,
        "area": area,
        "precio_m2": precio_m2,
        "precio_total": precio_total,
        "estado": "Disponible"
    }
    lotes.append(nuevo_lote)
    print(f"  [OK] Lote {codigo} registrado con éxito. Precio Total: S/ {precio_total:,.2f}")

def listar_lotes(lotes: list, solo_disponibles: bool = False):
    titulo = "LOTES DISPONIBLES" if solo_disponibles else "TODOS LOS LOTES"
    print(f"\n--- {titulo} ---")
    
    filtrados = [l for l in lotes if not solo_disponibles or l["estado"] == "Disponible"]
    if not filtrados:
        print("  No hay lotes registrados en esta categoría.")
        return

    print(f"{'Código':<10} | {'Urbanización':<15} | {'Área (m2)':<10} | {'Precio/m2':<12} | {'Precio Total':<14} | {'Estado'}")
    print("-" * 80)
    for l in filtrados:
        print(f"{l['codigo']:<10} | {l['urbanizacion']:<15} | {l['area']:<10.2f} | S/ {l['precio_m2']:<9.2f} | S/ {l['precio_total']:<11,.2f} | {l['estado']}")

def buscar_lote(lotes: list, codigo: str):
    for lote in lotes:
        if lote["codigo"].upper() == codigo.strip().upper():
            return lote
    return None