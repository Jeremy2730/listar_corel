from configuracion.orden_tallas import ORDEN_TALLAS


class ResumenProduccion:

    def __init__(
        self,
        conteo,
        no_reconocidos=None
    ):

        self.conteo = conteo
        self.no_reconocidos = no_reconocidos or {}

    def mostrar(self):

        agrupado = {}

        for clave, cantidad in self.conteo.items():

            producto, talla = clave.split(" ", 1)

            if talla not in agrupado:
                agrupado[talla] = {}

            agrupado[talla][producto] = cantidad

        print("\n===== PRODUCCION =====\n")

        for talla in ORDEN_TALLAS:

            if talla not in agrupado:
                continue

            print(f"\n--- {talla} ---")

            total_talla = 0

            for producto, cantidad in agrupado[talla].items():

                print(
                    f"{producto:<15} -> {cantidad}"
                )

                total_talla += cantidad

            print(f"Total {talla}: {total_talla}")

        print("\n===== ESTADISTICAS =====\n")

        reconocidos = sum(
            self.conteo.values()
        )

        no_reconocidos = sum(
            self.no_reconocidos.values()
        )

        print(
            f"Reconocidos: {reconocidos}"
        )

        print(
            f"No reconocidos: {no_reconocidos}"
        )

        if no_reconocidos > 0:

            print(
                "\n⚠ Existen piezas no reconocidas."
            )

            print(
                "Use la opcion de diagnostico "
                "para ver el detalle."
            )