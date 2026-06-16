from comparador.configuracion_pedidos import PEDIDOS


class ExpandidorPedido:

    def expandir(self, pedido):

        expandido = {}

        for clave_pedido, cantidad in pedido.items():

            if clave_pedido not in PEDIDOS:
                continue

            componentes = PEDIDOS[clave_pedido]

            for componente in componentes:

                expandido[componente] = (
                    expandido.get(componente, 0)
                    + cantidad
                )

        return expandido