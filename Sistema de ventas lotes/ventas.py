import calculos
import validaciones
import lotes as mod_lotes

def registrar_venta(lotes: list, ventas: list):
    print("\n--- REGISTRAR VENTA DE LOTE ---")
    codigo = validaciones.pedir_texto("Ingrese el código del lote a vender: ").upper()
    lote = mod_lotes.buscar_lote(lotes, codigo)

    if lote is None:
        print(f"  [Error] El lote '{codigo}' no existe.")
        return

    if lote["estado"] == "Vendido":
        print(f"  [Error] Operación rechazada: El lote '{codigo}' ya figura como VENDIDO.")
        return

    comprador = validaciones.pedir_texto("Nombre completo del comprador: ")
    documento = validaciones.pedir_texto("Documento de identidad (DNI/RUC): ")

    precio_total = lote["precio_total"]
    cuota_inicial = calculos.calcular_cuota_inicial(precio_total)
    saldo = calculos.calcular_saldo(precio_total, cuota_inicial)

    # Cambiar estado del lote a Vendido
    lote["estado"] = "Vendido"

    nueva_venta = {
        "codigo_lote": lote["codigo"],
        "urbanizacion": lote["urbanizacion"],
        "comprador": comprador,
        "documento": documento,
        "precio_total": precio_total,
        "cuota_inicial": cuota_inicial,
        "saldo": saldo
    }
    ventas.append(nueva_venta)

    print("\n  [OK] ¡Venta registrada exitosamente!")
    print("")
    print(f"  -> Lote: {lote['codigo']} ({lote['urbanizacion']})")
    print(f"  -> Comprador: {comprador} (Doc: {documento})")
    print(f"  -> Precio Total:  S/ {precio_total:,.2f}")
    print(f"  -> Cuota Inicial: S/ {cuota_inicial:,.2f} (20%)")
    print(f"  -> Saldo a pagar: S/ {saldo:,.2f}")

def mostrar_resumen_ventas(ventas: list):
    print("\n--- RESUMEN DE VENTAS REALIZADAS ---")
    if not ventas:
        print("  Aún no se han registrado ventas.")
        return

    print(f"{'Lote':<8} | {'Urbanización':<14} | {'Comprador':<20} | {'Doc.':<10} | {'Total':<13} | {'Inicial (20%)':<14} | {'Saldo'}")
    print("-" * 105)
    for v in ventas:
        print(f"{v['codigo_lote']:<8} | {v['urbanizacion']:<14} | {v['comprador']:<20} | {v['documento']:<10} | S/ {v['precio_total']:<10,.2f} | S/ {v['cuota_inicial']:<11,.2f} | S/ {v['saldo']:,.2f}")