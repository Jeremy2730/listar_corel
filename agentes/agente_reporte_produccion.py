class AgenteReporteProduccion:

    def trabajar(
        self,
        pedido_cliente,
        produccion_cliente,
        faltantes,
        sobrantes
    ):

        print(
            "\n===== RESUMEN CLIENTE =====\n"
        )

        for clave, cantidad in (
            produccion_cliente.items()
        ):

            print(
                f"{clave:<25} -> {cantidad}"
            )

        if faltantes:

            print(
                "\n===== FALTANTES =====\n"
            )

            for clave, cantidad in (
                faltantes.items()
            ):

                print(
                    f"{clave:<25} -> {cantidad}"
                )

        if sobrantes:

            print(
                "\n===== SOBRANTES =====\n"
            )

            for clave, cantidad in (
                sobrantes.items()
            ):

                print(
                    f"{clave:<25} -> {cantidad}"
                )

        if not faltantes and not sobrantes:

            print(
                "\nPEDIDO COMPLETO"
            )