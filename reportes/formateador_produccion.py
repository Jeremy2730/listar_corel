# formateador produccion

from configuracion.orden_tallas import ORDEN_TALLAS
from servicios.agrupador_tallas import agrupar_por_tallas


def mostrar_por_tallas(
    datos,
    titulo="PRODUCCION"
):

    agrupado = agrupar_por_tallas(
        datos
    )

    print(f"\n===== {titulo} =====")

    for talla in ORDEN_TALLAS:

        if talla not in agrupado:
            continue

        print(f"\n--- {talla} ---")

        total_talla = 0

        for producto in sorted(agrupado[talla]):

            cantidad = agrupado[talla][producto]

            print(
                f"{producto:<30} -> {cantidad}"
            )

            total_talla += cantidad

        print(
            f"\nTotal talla {talla:<18} -> {total_talla}"
        )

    total_general = sum(datos.values())

    print("\n--------------------")
    print(f"TOTAL GENERAL: {total_general}")


def mostrar_resumen(
    datos,
    titulo,
    no_reconocidos=None
):

    mostrar_por_tallas(datos, titulo)

    print("\n===== ESTADISTICAS =====\n")

    print(
        f"Reconocidos: {sum(datos.values())}"
    )

    if not no_reconocidos:

        print("No reconocidos: 0")
        return

    cantidad_no_reconocidos = sum(
        no_reconocidos.values()
    )

    print(
        f"No reconocidos: "
        f"{cantidad_no_reconocidos}"
    )

    ver = input(
        "\n¿Ver piezas no reconocidas? (S/N): "
    ).strip().upper()

    if ver == "S":

        print(
            "\n===== NO RECONOCIDOS =====\n"
        )

        for medida, cantidad in sorted(
            no_reconocidos.items()
        ):

            print(
                f"{medida:<30} -> {cantidad}"
            )


def ordenar_resumen(resumen):

    def clave_orden(item):

        clave = item[0]

        try:

            producto, talla = clave.rsplit(
                " ",
                1
            )

            if talla in ORDEN_TALLAS:

                posicion = ORDEN_TALLAS.index(
                    talla
                )

                return (
                    posicion,
                    producto
                )

        except ValueError:
            pass

        return (
            len(ORDEN_TALLAS),
            clave
        )

    return dict(
        sorted(
            resumen.items(),
            key=clave_orden
        )
    )

