from reportes.encabezados import mostrar_titulo

def mostrar_estado_pedido(
    pedido
):

    mostrar_titulo(
        "📋 Listado activo"
    )

    print(
        f"Nombre: {pedido['nombre']}"
    )

    documentos = pedido.get(
        "documentos",
        []
    )

    print(
        f"\nDocumentos: "
        f"{len(documentos)}\n"
    )

    for i, doc in enumerate(
        documentos,
        1
    ):

        print(
            f"  {i}. {doc['archivo']}"
        )

    print(
        f"\nPiezas acumuladas: "
        f"{sum(pedido['acumulado'].values())}"
    )

    print()


