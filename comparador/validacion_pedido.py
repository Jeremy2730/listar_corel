class ValidadorPedido:

    PRENDAS_VALIDAS = [
        "camiseta",
        "buso",
        "pantaloneta",
        "peto",
        "uniforme",
        "uniforme_buso",
        "uniforme_peto"
    ]

    def validar_prenda(self, prenda):

        prenda = prenda.strip().lower()

        if prenda in self.PRENDAS_VALIDAS:
            return prenda

        return None
    