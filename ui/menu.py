class Menu:

    def mostrar(self):

        print("\n===== LISTAR COREL =====\n")

        print("1. Crear listado")
        print("2. Administrar listado")
        print("3. Agregar documento al listado")
        print("4. Eliminar listado")
        print("5. Listar documento actual")
        print("6. Salir")

        return input(
            "\nSeleccione una opción: "
        ).strip()