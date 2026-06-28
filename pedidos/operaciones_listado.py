from servicios.pedido_servicio import PedidoServicio
from pedidos.estado_manager import EstadoManager
from reportes.formateador_acumulado import mostrar_acumulado
from reportes.formateador_produccion import mostrar_resumen
from reportes.formateador_estado import mostrar_estado_pedido
from reportes.formateador_listado import mostrar_listado
from servicios.selector_documento import seleccionar_documento
from servicios.documento_actual import obtener_documento_actual


class OperacionesListado:


    def __init__(self):

        self.pedido_servicio = PedidoServicio()
        self.estado_manager = EstadoManager()


    def ver_listado(self):

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print(
                "No existe listado guardado."
            )

            return

        mostrar_listado(
            pedido
        )


    def mostrar_estado_actual(self):

        if not self.estado_manager.hay_pedido_activo():

            print(
                "\nNo existe listado activo.\n"
            )

            return

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print(
                "\nNo existe listado activo.\n"
            )

            return

        mostrar_estado_pedido(
            pedido
        )


    def crear_listado(self):

        nombre_listado = input(
            "\nNombre del listado: "
        )

        nombre_documento, analizador = self._obtener_analizador()

        if not analizador:
            return

        mostrar_resumen(
            analizador.obtener_resumen(),
            "DOCUMENTO",
            analizador.obtener_no_reconocidos()
        )

        self.pedido_servicio.crear(

            nombre_listado,
            nombre_documento,
            analizador

        )

        self.estado_manager.marcar_pedido_activo()

        print(
            "\nListado guardado correctamente."
        )


    def administrar_listado(self):

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print("No existe listado guardado.")
            return


        while True:

            print("\n=== ADMINISTRAR LISTADO ===")
            print("1. Ver acumulado")
            print("2. Eliminar documento")
            print("3. Comparar pedido")
            print("4. Volver")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":

                self.ver_acumulado()

            elif opcion == "2":
                self.eliminar_documento()

            elif opcion == "3":
                self.menu_comparar_pedido()

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")


    def menu_comparar_pedido(self):

        while True:

            print("\n=== COMPARAR PEDIDO ===")
            print("1. Pedido manual")
            print("2. Pedido Excel")
            print("3. Volver")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.comparar_pedido_manual()

            elif opcion == "2":
                print("Función aún no implementada.")

            elif opcion == "3":
                break

            else:
                print("Opción inválida.")


    def agregar_documento(self):

        nombre_documento, analizador = self._obtener_analizador()

        if not analizador:
            return

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print(
                "No existe listado activo."
            )

            return

        for doc in pedido["documentos"]:

            if doc["archivo"] == nombre_documento:

                print(
                    "Ese documento ya fue agregado."
                )

                return

        mostrar_resumen(
            analizador.obtener_resumen(),
            "DOCUMENTO",
            analizador.obtener_no_reconocidos()
        )


        respuesta = input(
            "\nAgregar documento al listado? (s/n): "
        )

        if respuesta.lower() != "s":

            print(
                "Operacion cancelada."
            )

            return

        self.pedido_servicio.agregar_documento(

            pedido,
            nombre_documento,
            analizador

        )

        print(
            "\nDocumento agregado correctamente."
        )


    def eliminar_listado(self):

        if self.pedido_servicio.eliminar():

            self.estado_manager.marcar_sin_pedido()

            print(
                "Listado eliminado."
            )

        else:

            print(
                "No existe listado."
            )


    def listar_documento_actual(self):

        documento = self._obtener_documento()

        if not documento:
            return

        analizador = documento["analizador"]

        mostrar_resumen(
            analizador.obtener_resumen(),
            "DOCUMENTO ACTUAL",
            analizador.obtener_no_reconocidos()
        )


    def ver_acumulado(self):

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print(
                "\nNo existe listado activo."
            )

            return

        mostrar_acumulado(
            pedido
        )


    def eliminar_documento(self):

        pedido = self.pedido_servicio.obtener()

        if not pedido:

            print(
                "No existe listado activo."
            )

            return

        if not pedido["documentos"]:

            print(
                "No existen documentos."
            )

            return

        indice = seleccionar_documento(
            pedido["documentos"]
        )

        if indice is None:
            return

        eliminado = (
            self.pedido_servicio.eliminar_documento(
                pedido,
                indice
            )
        )

        print()

        print(
            f"Documento eliminado: "
            f"{eliminado['archivo']}"
        )

        print(
            "Acumulado recalculado."
        )


    def _obtener_documento(self):

        return obtener_documento_actual()
 
    
    def _obtener_analizador(self):

        documento = self._obtener_documento()

        if not documento:
            return None, None

        return (
            documento["nombre"],
            documento["analizador"]
        )