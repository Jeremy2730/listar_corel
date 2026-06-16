class Normalizador:

    def normalizar(self, prenda, talla):

        prenda = prenda.strip().lower()
        talla = talla.strip().upper()

        return prenda, talla