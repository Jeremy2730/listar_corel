class ReporteCliente:

    def convertir_produccion(
        self,
        prendas,
        conjuntos
    ):

        resultado = {}

        for clave, cantidad in conjuntos.items():

            resultado[clave] = cantidad

        for clave, cantidad in prendas.items():

            producto, talla = (
                clave.rsplit(" ", 1)
            )

            conjuntos_talla = conjuntos.get(
                f"conjunto {talla}",
                0
            )

            restante = cantidad - conjuntos_talla

            if restante > 0:

                resultado[clave] = restante

        return resultado