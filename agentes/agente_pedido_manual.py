from comparador.configuracion_prendas import PRENDAS
from configuracion.orden_tallas import ORDEN_TALLAS
from inventario.estante_pedidos import EstantePedidos


class AgentePedidoManual:

    def __init__(self):

        self.estante = EstantePedidos()

    def capturar(self):

        print("\n*** AGENTE PEDIDO MANUAL ACTIVO ***\n")

        pedido = {}

        for prenda in PRENDAS:

            print(f"\n===== {prenda.upper()} =====")

            for talla in ORDEN_TALLAS:

                texto = input(
                    f"{talla}: "
                ).strip()

                if not texto:
                    continue

                try:

                    cantidad = int(texto)

                    if cantidad > 0:

                        pedido[
                            f"{prenda} {talla}"
                        ] = cantidad

                except ValueError:

                    print("Valor inválido")

        # Guardar una sola vez
        self.estante.guardar(pedido)

        print("\n===== PEDIDO CAPTURADO =====\n")

        for clave, cantidad in pedido.items():

            print(
                f"{clave:<25} -> {cantidad}"
            )

        print(
            "\nPedidos almacenados:",
            len(self.estante.obtener_todos())
        )

        return pedido