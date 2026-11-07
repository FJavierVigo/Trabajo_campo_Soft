import lotes
import ventas

def mostrar_menu():
    print("\n==============================================")
    print("   SISTEMA DE VENTA DE LOTES - TERRENOS S.A.C.")
    print("==============================================")
    print("1. Registrar nuevo lote")
    print("2. Listar todos los lotes")
    print("3. Consultar lotes disponibles")
    print("4. Registrar venta de lote")
    print("5. Ver resumen de ventas")
    print("6. Salir")
    return input("Seleccione una opción (1-6): ").strip()

def main():
    lista_lotes = []
    lista_ventas = []

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            lotes.registrar_lote(lista_lotes)
        elif opcion == "2":
            lotes.listar_lotes(lista_lotes, solo_disponibles=False)
        elif opcion == "3":
            lotes.listar_lotes(lista_lotes, solo_disponibles=True)
        elif opcion == "4":
            ventas.registrar_venta(lista_lotes, lista_ventas)
        elif opcion == "5":
            ventas.mostrar_resumen_ventas(lista_ventas)
        elif opcion == "6":
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("  [Error] Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()