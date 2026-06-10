from catalogos.camisetas import CATALOGO_CAMISETAS
from catalogos.mangas import CATALOGO_MANGAS
from catalogos.mangas_largas import CATALOGO_MANGAS_LARGAS
from catalogos.pantalonetas import CATALOGO_PANTALONETAS


class BuscadorCatalogo:

    def __init__(self):

        self.catalogos = {
            "camiseta": CATALOGO_CAMISETAS,
            "manga": CATALOGO_MANGAS,
            "manga_larga": CATALOGO_MANGAS_LARGAS,
            "pantaloneta": CATALOGO_PANTALONETAS
        }

    def buscar(self, ancho, alto):

        ancho = round(ancho, 1)
        alto = round(alto, 1)

        medidas_shape = sorted([ancho, alto])

        mejor_match = None
        menor_error = float("inf")

        for producto, catalogo in self.catalogos.items():

            for talla, piezas in catalogo.items():

                for pieza, datos in piezas.items():

                    medidas_catalogo = sorted([
                        round(datos["ancho"], 1),
                        round(datos["alto"], 1)
                    ])

                    diferencia_ancho = abs(
                        medidas_shape[0] - medidas_catalogo[0]
                    )

                    diferencia_alto = abs(
                        medidas_shape[1] - medidas_catalogo[1]
                    )

                    error = (
                        diferencia_ancho +
                        diferencia_alto
                    )

                    if error < menor_error:

                        menor_error = error

                        mejor_match = {
                            "producto": producto,
                            "talla": talla,
                            "pieza": pieza
                        }

        if menor_error <= 1:

            return mejor_match

        return None