from corel.corel_api import CorelAPI
from analizadores.analizador_piezas import AnalizadorPiezas
from pedidos.resumen_produccion import ResumenProduccion
from pedidos.pedido_manager import PedidoManager
from pedidos.estado_manager import EstadoManager
from datetime import date


class OperacionesListado:

    def __init__(self):

        self.pedido_manager = PedidoManager()
        self.estado_manager = EstadoManager()

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