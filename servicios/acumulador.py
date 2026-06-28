# acumulador

def recalcular_acumulado(
    documentos
):

    acumulado = {}

    for documento in documentos:

        for clave, cantidad in (
            documento["resumen"].items()
        ):

            acumulado[clave] = (

                acumulado.get(
                    clave,
                    0
                )

                + cantidad
            )

    return acumulado