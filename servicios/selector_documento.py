# selector_documento.py

def seleccionar_documento(
    documentos
):

    print(
        "\n===== SELECCIONAR DOCUMENTO =====\n"
    )

    for i, doc in enumerate(
        documentos,
        start=1
    ):

        print(
            f"{i}. {doc['archivo']}"
        )

    opcion = input(
        "\nNumero del documento: "
    )

    try:

        indice = int(opcion) - 1

    except ValueError:

        print(
            "Debe ingresar un numero."
        )

        return None

    if indice < 0 or indice >= len(
        documentos
    ):

        print(
            "Documento inexistente."
        )

        return None

    return indice