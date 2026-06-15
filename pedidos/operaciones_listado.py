from corel.corel_api import CorelAPI
from analizadores.analizador_piezas import AnalizadorPiezas
from pedidos.resumen_documento import ResumenDocumento
from pedidos.resumen_produccion import ResumenProduccion
from pedidos.pedido_manager import PedidoManager
from pedidos.estado_manager import EstadoManager
from datetime import date
from configuracion.orden_tallas import ORDEN_TALLAS
from comparador.comparador_pedido import ComparadorPedido
from comparador.ensamblador_prendas import EnsambladorPrendas

class OperacionesListado:


    def __init__(self):

        self.pedido_manager = PedidoManager()
        self.estado_manager = EstadoManager()
        self.comparador = ComparadorPedido()
        self.ensamblador = EnsambladorPrendas()


    def ver_listado(self):

        pedido = self.pedido_manager.cargar()

        if not pedido:

            print(
                "No existe listado guardado."
            )

            return

        print("\n===== LISTADO ACTIVO =====\n")

        print(f"Nombre: {pedido['nombre']}")
        print(f"Fecha: {pedido['fecha']}")

        print("\nDocumentos cargados:\n")

        for i, doc in enumerate(
            pedido["documentos"],
            start=1
        ):

            print(
                f"{i}. {doc['archivo']}"
            )

        print()

        print(
            f"Total documentos: "
            f"{len(pedido['documentos'])}"
        )


    def mostrar_estado_actual(self):

        if not self.estado_manager.hay_pedido_activo():

            print(
                "\nNo existe listado activo.\n"
            )

            return

        pedido = self.pedido_manager.cargar()

        if not pedido:

            print(
                "\nNo existe listado activo.\n"
            )

            return

        print("\n==========================")
        print(
            f"📋 Listado activo "
        )
        print("==========================\n")       

        print(
            f"Nombre: "
            f"{pedido['nombre']}"
        )

        print(
            f"Documentos: "
            f"{len(pedido['documentos'])}"
        )

        total = sum(
            pedido["acumulado"].values()
        )

        print(
            f"Piezas acumuladas: {total}"
        )

        print()


    def crear_listado(self):

        nombre_listado = input(
            "\nNombre del listado: "
        )

        corel = CorelAPI()

        if not corel.conectar():
            return

        print()
        print("DOCUMENTO:")
        print(corel.doc.Name)
        print()

        nombre_documento = corel.doc.Name

        analizador = AnalizadorPiezas()

        for shape in corel.obtener_shapes():
            analizador.analizar(shape)

        resumen = ResumenProduccion(
            analizador.obtener_resumen(),
            analizador.obtener_no_reconocidos()
        )

        resumen.mostrar()

        datos_pedido = {

            "nombre": nombre_listado,

            "fecha": str(date.today()),

            "documentos": [
                {
                    "archivo": nombre_documento,
                    "resumen": analizador.obtener_resumen()
                }
            ],

            "acumulado": analizador.obtener_resumen()
        }

        self.pedido_manager.guardar(
            datos_pedido
        )

        self.estado_manager.marcar_pedido_activo()

        print(
            "\nListado guardado correctamente."
        )


    def administrar_listado(self):

        pedido = self.pedido_manager.cargar()

        if not pedido:

            print("No existe listado guardado.")
            return


        while True:

            print("\n=== ADMINISTRAR LISTADO ===")
            print("1. Ver acumulado")
            print("2. Eliminar documento")
            print("3. Comparar pedido")
            print("4. Volver")

            opcion = input("Seleccione una opción: ").strip()

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

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.comparar_pedido_manual()

            elif opcion == "2":
                print("Función aún no implementada.")

            elif opcion == "3":
                break

            else:
                print("Opción inválida.")


    def comparar_pedido_manual(self):

        pedido_manual = (
            self.comparador
            .capturar_pedido_manual()
        )

        pedido_guardado = (
            self.pedido_manager.cargar()
        )

        produccion = self.ensamblador.obtener_prendas(
            pedido_guardado["acumulado"]
        )

        resultado, faltantes, sobrantes = (

            self.comparador.comparar_pedido(
                pedido_manual,
                produccion
            )
        )

        self.comparador.mostrar_comparacion(
            resultado,
            faltantes,
            sobrantes
        )


    def agregar_documento(self):

        pedido = self.pedido_manager.cargar()

        if not pedido:

            print(
                "No existe listado activo."
            )

            return

        corel = CorelAPI()

        if not corel.conectar():
            return

        nombre_documento = corel.doc.Name

        print()
        print("DOCUMENTO:")
        print(nombre_documento)
        print()

        for doc in pedido["documentos"]:

            if doc["archivo"] == nombre_documento:

                print(
                    "Ese documento ya fue agregado."
                )

                return

        analizador = AnalizadorPiezas()

        for shape in corel.obtener_shapes():

            analizador.analizar(shape)

        resumen = ResumenProduccion(
            analizador.obtener_resumen(),
            analizador.obtener_no_reconocidos()
        )

        resumen.mostrar()

        respuesta = input(
            "\nAgregar documento al listado? (s/n): "
        )

        if respuesta.lower() != "s":

            print(
                "Operacion cancelada."
            )

            return

        nuevo_documento = {

            "archivo": nombre_documento,

            "resumen": analizador.obtener_resumen()
        }

        pedido["documentos"].append(
            nuevo_documento
        )

        for clave, cantidad in (
            analizador.obtener_resumen().items()
        ):

            pedido["acumulado"][clave] = (

                pedido["acumulado"].get(
                    clave,
                    0
                )

                + cantidad
            )

        self.pedido_manager.guardar(
            pedido
        )

        print(
            "\nDocumento agregado correctamente."
        )


    def eliminar_listado(self):

        if self.pedido_manager.eliminar():

            self.estado_manager.marcar_sin_pedido()

            print(
                "Listado eliminado."
            )

        else:

            print(
                "No existe listado."
            )


    def listar_documento_actual(self):

        corel = CorelAPI()

        if not corel.conectar():
            return

        print()
        print("DOCUMENTO:")
        print(corel.doc.Name)
        print()

        analizador = AnalizadorPiezas()

        for shape in corel.obtener_shapes():
            analizador.analizar(shape)


        resumen = ResumenDocumento(
            analizador.obtener_resumen(),
            analizador.obtener_no_reconocidos()
        )

        resumen.mostrar()


    def ver_acumulado(self):

        pedido = self.pedido_manager.cargar()

        if not pedido["acumulado"]:

            print(
                "\nNo hay piezas reconocidas."
            )

            return

        acumulado = self.ordenar_resumen(
            pedido["acumulado"]
        )

        print("\n===== ACUMULADO =====\n")

        for clave, cantidad in acumulado.items():

            print(
                f"{clave:<20} -> {cantidad}"
            )
        prendas = self.ensamblador.obtener_prendas(
            pedido["acumulado"]
        )

        incompletos = self.ensamblador.obtener_incompletos(
            pedido["acumulado"]
        )


        if prendas:

            print("\n===== PRENDAS =====\n")

            for clave, cantidad in prendas.items():

                print(
                    f"{clave:<25} -> {cantidad}"
                )

        if incompletos:

            print("\n===== INCOMPLETOS =====\n")

            for item in incompletos:

                print(
                    f"{item['prenda']} {item['talla']}"
                )

                for pieza, cantidad in (
                    item["piezas"].items()
                ):

                    print(
                        f"  {pieza:<20}: {cantidad}"
                    )

                print()  


    def eliminar_documento(self):

        pedido = self.pedido_manager.cargar()

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

        print("\n===== ELIMINAR DOCUMENTO =====\n")

        for i, doc in enumerate(
            pedido["documentos"],
            start=1
        ):

            print(
                f"{i}. {doc['archivo']}"
            )

        opcion = input(
            "\nNumero del documento: "
        )

        try:

            indice = int(opcion) - 1

        except ValueError:

            print(
                "Debe ingresar un numero."
            )

            return

        if indice < 0 or indice >= len(
            pedido["documentos"]
        ):

            print(
                "Documento inexistente."
            )

            return

        eliminado = pedido[
            "documentos"
        ].pop(indice)

        acumulado = {}

        for documento in pedido[
            "documentos"
        ]:

            for clave, cantidad in (
                documento["resumen"].items()
            ):

                acumulado[clave] = (

                    acumulado.get(
                        clave,
                        0
                    )

                    + cantidad
                )

        pedido["acumulado"] = acumulado

        self.pedido_manager.guardar(
            pedido
        )

        print()

        print(
            f"Documento eliminado: "
            f"{eliminado['archivo']}"
        )

        print(
            "Acumulado recalculado."
        )


    @staticmethod
    def ordenar_resumen(resumen):

        orden = {}

        for clave, cantidad in resumen.items():

            producto, talla = clave.rsplit(" ", 1)

            if talla in ORDEN_TALLAS:
                posicion = ORDEN_TALLAS.index(talla)
            else:
                posicion = 999

            orden[clave] = (
                posicion,
                producto
            )

        return dict(
            sorted(
                resumen.items(),
                key=lambda x: orden[x[0]]
            )
        )  