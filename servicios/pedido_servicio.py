from pedidos.pedido_manager import PedidoManager
from datetime import date
from pedidos.fabrica_documento import crear_documento
from servicios.acumulador import recalcular_acumulado


class PedidoServicio:

    def __init__(self):

        self.manager = PedidoManager()


    def obtener(self):

        return self.manager.cargar()


    def guardar(
        self,
        pedido
    ):

        self.manager.guardar(
            pedido
        )


    def eliminar(self):

        return self.manager.eliminar()


    def agregar_documento(
        self,
        pedido,
        nombre_documento,
        analizador
    ):

        documento = crear_documento(
            nombre_documento,
            analizador
        )

        pedido["documentos"].append(
            documento
        )

        for clave, cantidad in documento["resumen"].items():

            pedido["acumulado"][clave] = (
                pedido["acumulado"].get(
                    clave,
                    0
                )
                + cantidad
            )

        self.guardar(
            pedido
        )


    def crear(
        self,
        nombre_listado,
        nombre_documento,
        analizador
    ):

        pedido = {

            "nombre": nombre_listado,

            "fecha": str(date.today()),

            "documentos": [

                crear_documento(
                    nombre_documento,
                    analizador
                )

            ],

            "acumulado": analizador.obtener_resumen()

        }

        self.guardar(
            pedido
        )

        return pedido
 
    
    def eliminar_documento(
        self,
        pedido,
        indice
    ):

        eliminado = pedido["documentos"].pop(
            indice
        )

        pedido["acumulado"] = (
            recalcular_acumulado(
                pedido["documentos"]
            )
        )

        self.guardar(
            pedido
        )

        return eliminado

