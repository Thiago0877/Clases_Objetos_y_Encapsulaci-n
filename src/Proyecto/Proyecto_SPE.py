import datetime

# Diccionario principal que almacena el inventario de equipos
# Cada equipo tiene: disponible (bool) y prestamos (lista de tuplas)
equipos = {
    "Laptop Dell": {"disponible": True, "prestamos": []},
    "Proyector Epson": {"disponible": True, "prestamos": []},
    "Tablet Samsung": {"disponible": True, "prestamos": []},
}


def mostrar_equipos():
    print("\n=== Inventario de Equipos ===")
    for equipo, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"- {equipo} | Estado: {estado}")
    print()


def registrar_prestamo():
    mostrar_equipos()
    equipo = input("Ingrese el nombre exacto del equipo a prestar: ")

    if equipo not in equipos:
        print("❌ El equipo no existe en el sistema.")
        return

    if not equipos[equipo]["disponible"]:
        print("❌ El equipo ya está prestado.")
        return

    usuario = input("Ingrese el nombre del usuario que solicita el préstamo: ")
    fecha = datetime.date.today().strftime("%d/%m/%Y")

    # Se guarda el préstamo como tupla (usuario, fecha)
    equipos[equipo]["prestamos"].append((usuario, fecha))
    equipos[equipo]["disponible"] = False
    print(f"✅ El equipo '{equipo}' ha sido prestado a {usuario} el {fecha}.")


def devolver_equipo():
    equipo = input("Ingrese el nombre exacto del equipo a devolver: ")

    if equipo not in equipos:
        print("❌ El equipo no existe en el sistema.")
        return

    if equipos[equipo]["disponible"]:
        print("⚠️ El equipo ya estaba disponible en el inventario.")
        return

    equipos[equipo]["disponible"] = True
    print(f"✅ El equipo '{equipo}' ha sido devuelto y está disponible nuevamente.")


def ver_historial():
    print("\n=== Historial de Préstamos ===")
    for equipo, datos in equipos.items():
        print(f"\n📌 {equipo}:")
        if datos["prestamos"]:
            for i, prestamo in enumerate(datos["prestamos"], 1):
                usuario, fecha = prestamo
                print(f"  {i}. Usuario: {usuario} | Fecha: {fecha}")
        else:
            print("  Sin préstamos registrados.")
    print()


def agregar_equipo():
    equipo = input("Ingrese el nombre del nuevo equipo: ")

    if equipo in equipos:
        print("⚠️ El equipo ya existe en el sistema.")
        return

    equipos[equipo] = {"disponible": True, "prestamos": []}
    print(f"✅ El equipo '{equipo}' ha sido agregado al inventario.")


def menu():
    while True:
        print("\n===== Sistema de Préstamos de Equipos =====")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
