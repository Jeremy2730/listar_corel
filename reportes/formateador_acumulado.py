# reportes/formateador_acumulado.py

from configuracion.orden_tallas import ORDEN_TALLAS

def mostrar_documento_acumulado(
    doc
):

    print(
        f"\n===== {doc['archivo']} =====\n"
    )

    total_reconocidas = 0

    for clave, cantidad in sorted(
        doc["resumen"].items()
    ):

        print(
            f"{clave:<30} -> {cantidad}"
        )

        total_reconocidas += cantidad

    nombradas = {}
    sin_nombre = {}

    for clave, cantidad in (
        doc.get(
            "no_reconocidos",
            {}
        ).items()
    ):

        if "|" in clave:

            nombradas[clave] = cantidad

        else:

            sin_nombre[clave] = cantidad

    if nombradas:

        print(
            "\nNO RECONOCIDAS NOMBRADAS\n"
        )

        for clave, cantidad in sorted(
            nombradas.items()
        ):

            print(
                f"{clave:<30} -> {cantidad}"
            )

    if sin_nombre:

        print(
            "\nNO RECONOCIDAS\n"
        )

        for clave, cantidad in sorted(
            sin_nombre.items()
        ):

            print(
                f"{clave:<30} -> {cantidad}"
            )

    total_no_reconocidas = sum(
        doc.get(
            "no_reconocidos",
            {}
        ).values()
    )

    print()

    print(
        f"Total reconocidas -> "
        f"{total_reconocidas}"
    )

    print(
        f"Total no reconocidas -> "
        f"{total_no_reconocidas}"
    )


def mostrar_resumen_acumulado(
    pedido
):

    total_documentos = len(
        pedido["documentos"]
    )

    total_no_reconocidas = 0

    for doc in pedido["documentos"]:

        total_no_reconocidas += sum(
            doc.get(
                "no_reconocidos",
                {}
            ).values()
        )

    print("\n==========================")
    print("RESUMEN ACUMULADO")
    print("==========================\n")

    print(
        f"Documentos -> "
        f"{total_documentos}"
    )

    print(
        f"Reconocidas -> "
        f"{sum(pedido['acumulado'].values())}"
    )

    print(
        f"No reconocidas -> "
        f"{total_no_reconocidas}"
    )


def mostrar_acumulado(
    pedido
):

    print("\n==========================")
    print("📋 LISTADO ACUMULADO")
    print("==========================\n")

    print(
        f"Nombre: {pedido['nombre']}"
    )

    print(
        f"Documentos: "
        f"{len(pedido['documentos'])}"
    )

    for doc in pedido["documentos"]:

        mostrar_documento_acumulado(
            doc
        )

    mostrar_resumen_acumulado(
        pedido
    )


