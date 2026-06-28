# formateador listado

def mostrar_listado(
    pedido
):

    print("\n===== LISTADO ACTIVO =====\n")

    print(f"Nombre: {pedido['nombre']}")
    print(f"Fecha: {pedido['fecha']}")

    print("\nDocumentos cargados:")

    for i, doc in enumerate(
        pedido["documentos"],
        start=1
    ):

        print(
            f"{i}. {doc['archivo']}"
        )

    print()

    print(
        f"Total documentos: "
        f"{len(pedido['documentos'])}"
    )