class ParserPedido:

    def parsear(self, texto: str):
        """
        Convierte:
        "1 camiseta xl, 2 uniforme m"

        en:
        [
            (1, "camiseta", "xl"),
            (2, "uniforme", "m")
        ]
        """

        resultado = []

        bloques = texto.split(",")

        for bloque in bloques:

            partes = bloque.strip().split()

            if len(partes) != 3:
                continue

            try:
                cantidad = int(partes[0])
                prenda = partes[1]
                talla = partes[2]

                resultado.append((cantidad, prenda, talla))

            except ValueError:
                continue

        return resultado