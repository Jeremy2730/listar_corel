from configuracion.orden_tallas import ORDEN_TALLAS
from comparador.configuracion_pedidos import PEDIDOS
from comparador.configuracion_prendas import PRENDAS


class EnsambladorPrendas:

    def obtener_prendas(self, resumen):

        prendas = {}

        for talla in ORDEN_TALLAS:

            for nombre_pedido, lista_prendas in PEDIDOS.items():

                for prenda in lista_prendas:

                    piezas = PRENDAS[prenda]

                    cantidades = []

                    for pieza in piezas:

                        cantidades.append(
                            resumen.get(
                                f"{pieza} {talla}",
                                0
                            )
                        )

                    ensambladas = min(cantidades)

                    if ensambladas > 0:

                        key = f"{nombre_pedido} {talla}"

                        prendas[key] = prendas.get(key, 0) + ensambladas

        return prendas


    def obtener_piezas_prenda(
        self,
        resumen,
        talla,
        nombre_prenda
    ):

        piezas = {}

        for pieza in PRENDAS[nombre_prenda]:

            piezas[pieza] = resumen.get(
                f"{pieza} {talla}",
                0
            )

        return piezas

    def obtener_incompletos(self, resumen):

        incompletos = []

        for talla in ORDEN_TALLAS:

            for nombre_pedido, lista_prendas in PEDIDOS.items():

                for prenda in lista_prendas:

                    piezas = self.obtener_piezas_prenda(
                        resumen,
                        talla,
                        prenda
                    )

                    maximo = max(piezas.values())

                    if maximo == 0:
                        continue

                    ensambladas = min(piezas.values())

                    if ensambladas < maximo:

                        incompletos.append({

                            "pedido": nombre_pedido,
                            "prenda": prenda,
                            "talla": talla,
                            "piezas": piezas

                        })

        return incompletos