#comparador pedido

from configuracion.orden_tallas import ORDEN_TALLAS
from comparador.configuracion_prendas import PRENDAS


class ComparadorPedido: 
 
    def capturar_pedido_manual(self):

        pedido = {}

        for nombre_prenda in PRENDAS:

            print(
                f"\n===== PEDIDO {nombre_prenda.upper()} ====="
            )

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
                            f"{nombre_prenda} {talla}"
                        ] = cantidad

                except ValueError:

                    print(
                        "Valor inválido"
                    )

        return pedido


    def obtener_claves_ordenadas(self):

        claves = []

        for nombre_prenda in PRENDAS:

            for talla in ORDEN_TALLAS:

                claves.append(
                    f"{nombre_prenda} {talla}"
                )

        return claves


    def comparar_pedido(
        self,
        pedido,
        produccion
    ):

        resultado = []

        faltantes_totales = 0
        sobrantes_totales = 0

        for clave in self.obtener_claves_ordenadas():

            if (
                clave not in pedido
                and clave not in produccion
            ):
                continue

            solicitado = pedido.get(
                clave,
                0
            )

            producido = produccion.get(
                clave,
                0
            )

            diferencia = producido - solicitado

            if diferencia == 0:

                estado = "COMPLETO"

            elif diferencia > 0:

                estado = f"SOBRAN {diferencia}"

                sobrantes_totales += diferencia

            else:

                estado = f"FALTAN {abs(diferencia)}"

                faltantes_totales += abs(
                    diferencia
                )

            resultado.append({

                "prenda": clave,

                "pedido": solicitado,

                "producido": producido,

                "estado": estado
            })

        return (
            resultado,
            faltantes_totales,
            sobrantes_totales
        )


    def mostrar_comparacion(
        self,
        resultado,
        faltantes,
        sobrantes
    ):

        print("\n" + "=" * 60)
        print("COMPARACION DE PEDIDO")
        print("=" * 60)

        for fila in resultado:

            print(
                f"{fila['prenda']:<25}"
                f"Pedido:{fila['pedido']:>4}   "
                f"Prod:{fila['producido']:>4}   "
                f"{fila['estado']}"
            )

        print("=" * 60)
        print(f"Faltantes totales : {faltantes}")
        print(f"Sobrantes totales : {sobrantes}")


