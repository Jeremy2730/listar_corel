from configuracion.orden_tallas import ORDEN_TALLAS

class EnsambladorConjuntos:

    def obtener_conjuntos(self, prendas):

        conjuntos = {}

        for talla in ORDEN_TALLAS:

            camiseta = prendas.get(
                f"camiseta {talla}",
                0
            )

            pantaloneta = prendas.get(
                f"pantaloneta {talla}",
                0
            )

            cantidad = min(
                camiseta,
                pantaloneta
            )

            if cantidad > 0:

                conjuntos[
                    f"conjunto {talla}"
                ] = cantidad

        return conjuntos