from comparador.ensamblador_prendas import EnsambladorPrendas
from configuracion.orden_tallas import ORDEN_TALLAS
from servicios.agrupador_tallas import agrupar_por_tallas


class ResumenProduccion:

    def __init__(
        self,
        conteo,
        no_reconocidos=None
    ):

        self.conteo = conteo
        self.no_reconocidos = no_reconocidos or {}

    def mostrar(self):

        agrupado = agrupar_por_tallas(
            self.conteo
        )


        ensamblador = EnsambladorPrendas()

        prendas = ensamblador.obtener_prendas(
            self.conteo
        )

        incompletos = ensamblador.obtener_incompletos(
            self.conteo
        )

        if prendas:

            print("\n===== PRENDAS =====\n")

            for clave, cantidad in prendas.items():

                print(
                    f"{clave:<20} -> {cantidad}"
                )

        if incompletos:

            print("\n===== INCOMPLETOS =====\n")

            for item in incompletos:

                print(
                    f"{item['prenda']} {item['talla']}"
                )

                for pieza, cantidad in item["piezas"].items():

                    print(
                        f"  {pieza:<18}: {cantidad}"
                    )

                print()     

        print("\n===== PRODUCCION =====\n")

        for talla in ORDEN_TALLAS:
            
            if talla not in agrupado:
                continue

            print(f"\n--- {talla} ---")

            total_talla = 0

            for producto, cantidad in agrupado[talla].items():

                print(
                    f"{producto:<20} -> {cantidad}"
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